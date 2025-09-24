"""
WAV Blade Damping Toolkit (Python 3.10)
--------------------------------------

Функции для анализа сигналов акселерометра из WAV:
- чтение канала
- вывод сырого сигнала
- спектр и распределение по гармоникам (поиск пиков)
- выделение гармоник (узкополосные компоненты)
- аппроксимация затухания (экспонента по огибающей)
- энергия сигнала и модальная (по компонентам) энергия
- декременты затухания по каждой гармонике
- декремент затухания суммарного аппроксимированного сигнала
- декремент суммарной энергии

Зависимости: numpy, scipy (io.wavfile, signal), matplotlib (для графиков), pandas (для табличного вывода).

Примечание:
- "энергия" без знания масс/жесткости рассматривается как энергетическая характеристика сигнала: ∫ y^2 dt.
- Для декремента суммарного сигнала и энергии вводится эффективная частота f_eff, взвешенная по энергии компонент.
"""

from __future__ import annotations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, hilbert, find_peaks, get_window

# -------------------- УТИЛИТЫ --------------------

def read_wav_channel(path: str, channel: int = 0, detrend: bool = True) -> Tuple[int, np.ndarray]:
    """Читает WAV и возвращает (fs, x) для выбранного канала в формате float32.
    Если файл моно — channel игнорируется. Выполняет простое удаление тренда (вычитание среднего).
    """
    fs, data = wavfile.read(path)
    if data.ndim == 1:
        x = data.astype(np.float64)
    else:
        x = data[:, channel].astype(np.float64)
    # Нормализация целочисленных форматов к [-1, 1]
    if np.issubdtype(data.dtype, np.integer):
        maxv = np.iinfo(data.dtype).max
        x = x / maxv
    if detrend:
        x = x - np.mean(x)
    return fs, x.astype(np.float64)


def plot_raw_signal(fs: int, x: np.ndarray, title: str = "Сырой сигнал", seconds: Optional[float] = None) -> None:
    """Строит сигнал во времени. Если seconds задано — рисует только первые секунды."""
    N = len(x)
    if seconds is not None:
        N = min(N, int(seconds * fs))
    t = np.arange(N) / fs
    plt.figure(figsize=(11, 3))
    plt.plot(t, x[:N])
    plt.xlabel("Время, с")
    plt.ylabel("Амплитуда")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def compute_spectrum(fs: int, x: np.ndarray, window: str = "hann") -> Tuple[np.ndarray, np.ndarray]:
    """Возвращает (freqs, amp) — односторонний модуль спектра rFFT с оконной функцией."""
    N = len(x)
    w = get_window(window, N, fftbins=True)
    X = np.fft.rfft(x * w)
    freqs = np.fft.rfftfreq(N, 1 / fs)
    amp = np.abs(X)
    return freqs, amp


def plot_spectrum(freqs: np.ndarray, amp: np.ndarray, title: str = "Спектр (амплитуда)", xlim: Optional[Tuple[float, float]] = None) -> None:
    plt.figure(figsize=(11, 3))
    plt.semilogy(freqs, amp)
    if xlim: plt.xlim(*xlim)
    plt.xlabel("Частота, Гц")
    plt.ylabel("Амплитуда (лог)")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def find_harmonic_peaks(freqs: np.ndarray, amp: np.ndarray, height_frac: float = 0.1, distance_hz: float = 5.0, max_peaks: int = 6) -> np.ndarray:
    """Находит индексы основных пиков спектра.
    height_frac — порог по высоте относительно max амплитуды.
    distance_hz — минимальное расстояние между пиками в Гц.
    max_peaks — ограничение на число пиков.
    """
    if len(freqs) < 3:
        return np.array([], dtype=int)
    # Переведем distance_hz в индексы по шагу частоты
    df = freqs[1] - freqs[0] if len(freqs) > 1 else 1.0
    min_distance = max(int(distance_hz / df), 1)
    peaks, props = find_peaks(amp, height=np.max(amp) * height_frac, distance=min_distance)
    # Отсортировать по убыванию амплитуды и взять top-K
    order = np.argsort(props["peak_heights"])[::-1]
    peaks = peaks[order][:max_peaks]
    # Отсортировать по частоте для удобства
    peaks = np.sort(peaks)
    return peaks


def bandpass_filter(fs: int, x: np.ndarray, f0: float, bw: float) -> np.ndarray:
    """Полосовой фильтр Баттерворта 4-го порядка вокруг f0 с шириной полосы bw (Гц)."""
    nyq = fs / 2
    low = max((f0 - bw / 2) / nyq, 1e-5)
    high = min((f0 + bw / 2) / nyq, 0.99999)
    if not (0 < low < high < 1):
        return np.zeros_like(x)
    b, a = butter(4, [low, high], btype="band")
    return filtfilt(b, a, x)


def analytic_envelope(y: np.ndarray) -> np.ndarray:
    """Огибающая через аналитический сигнал (Хильберт)."""
    return np.abs(hilbert(y))


def fit_exponential_decay(t: np.ndarray, a: np.ndarray, min_frac: float = 0.05) -> Tuple[float, float]:
    """Линейная регрессия ln(a) = c0 + c1 t на диапазоне, где a > min_frac*max(a).
    Возвращает (c0, c1), где c1<0 — скорость затухания в терминах ln-огибающей.
    """
    a = np.asarray(a)
    mask = a > (np.max(a) * min_frac)
    if np.count_nonzero(mask) < 10:
        mask = np.ones_like(a, dtype=bool)
    y = np.log(a[mask] + 1e-12)
    T = t[mask]
    A = np.vstack([np.ones_like(T), T]).T
    (c0, c1), *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(c0), float(c1)

# -------------------- ДАТАКЛАСС КОМПОНЕНТЫ --------------------

@dataclass
class HarmonicComponent:
    f0: float
    bw: float
    signal: np.ndarray  # y_k(t)
    envelope: np.ndarray  # |analytic|
    delta: float  # лог. декремент за период этой гармоники
    zeta: float   # коэффициент затухания ≈ δ/(2π)
    energy: float # ∫ y_k^2 dt

# -------------------- ОСНОВНЫЕ ПРОЦЕДУРЫ --------------------

def decompose_into_harmonics(fs: int, x: np.ndarray, peaks_idx: np.ndarray, freqs: np.ndarray, amp: np.ndarray,
                             bw_rule: str = "relative", bw_hz: float = 10.0, bw_rel: float = 0.2) -> List[HarmonicComponent]:
    """Выделяет гармоники по найденным пикам и оценивает их декременты и энергии.
    bw_rule: "fixed" (использовать bw_hz) или "relative" (bw = min(0.6*f0, bw_rel*f0, 30 Гц)).
    """
    dt = 1 / fs
    t = np.arange(len(x)) * dt
    components: List[HarmonicComponent] = []
    for idx in peaks_idx:
        f0 = float(freqs[idx])
        if bw_rule == "fixed":
            bw = bw_hz
        else:
            bw = min(0.6 * f0, bw_rel * f0, 30.0)
            bw = max(bw, 2.0)
        y = bandpass_filter(fs, x, f0, bw)
        env = analytic_envelope(y)
        c0, c1 = fit_exponential_decay(t, env)
        # δ за период T=1/f0: ln(ампл(t)/ампл(t+T)) ≈ -c1 * T
        delta = max(0.0, -c1 / f0)
        zeta = delta / (2 * np.pi)
        energy = float(np.trapz(y ** 2, dx=dt))
        components.append(HarmonicComponent(f0=f0, bw=bw, signal=y, envelope=env, delta=delta, zeta=zeta, energy=energy))
    return components


def plot_harmonics_time(fs: int, components: List[HarmonicComponent], max_plots: int = 6) -> None:
    """Рисует во времени выделенные гармоники (сигнал и огибающая)."""
    dt = 1 / fs
    t = np.arange(len(components[0].signal)) * dt if components else np.array([])
    for i, comp in enumerate(components[:max_plots], start=1):
        plt.figure(figsize=(11, 3))
        plt.plot(t, comp.signal, label=f"{comp.f0:.1f} Гц, bw={comp.bw:.1f} Гц")
        plt.plot(t, comp.envelope, linestyle="--", label=f"env (δ={comp.delta:.4f}, ζ={comp.zeta:.4f})")
        plt.xlabel("Время, с")
        plt.ylabel("Амплитуда")
        plt.title(f"Гармоника #{i}")
        plt.legend()
        plt.tight_layout()
        plt.show()


def components_table(components: List[HarmonicComponent]) -> pd.DataFrame:
    """Возвращает таблицу по компонентам: частота, полоса, энергия, δ, ζ."""
    rows = []
    for i, c in enumerate(components, start=1):
        rows.append({
            "#": i,
            "f0, Hz": c.f0,
            "bw, Hz": c.bw,
            "Energy ∫y² dt": c.energy,
            "δ per period": c.delta,
            "ζ ≈ δ/(2π)": c.zeta,
        })
    return pd.DataFrame(rows)


def reconstruct_sum(components: List[HarmonicComponent]) -> np.ndarray:
    """Суммирует выделенные гармоники."""
    if not components:
        return np.array([])
    Y = np.zeros_like(components[0].signal)
    for c in components:
        Y = Y + c.signal
    return Y


def effective_frequency_by_energy(components: List[HarmonicComponent]) -> float:
    """Эффективная частота для суммарных метрик: f_eff = Σ(E_k * f_k)/Σ(E_k)."""
    if not components:
        return np.nan
    Ek = np.array([c.energy for c in components])
    fk = np.array([c.f0 for c in components])
    if np.allclose(Ek.sum(), 0):
        return np.nan
    return float((Ek * fk).sum() / Ek.sum())


def total_signal_damping(fs: int, y: np.ndarray, f_ref: Optional[float] = None) -> Dict[str, float]:
    """Декремент для суммарного сигнала по огибающей. Если f_ref не задана — берется по максимуму спектра."""
    dt = 1 / fs
    t = np.arange(len(y)) * dt
    env = analytic_envelope(y)
    c0, c1 = fit_exponential_decay(t, env)
    # если не задана опорная частота — возьмем по максимуму спектра
    if f_ref is None:
        freqs, amp = compute_spectrum(fs, y)
        f_ref = float(freqs[np.argmax(amp)]) if len(freqs) else np.nan
    delta = max(0.0, -c1 / f_ref) if f_ref and f_ref > 0 else np.nan
    zeta = delta / (2 * np.pi) if delta == delta else np.nan
    energy = float(np.trapz(y ** 2, dx=dt))
    return {"delta": delta, "zeta": zeta, "energy": energy, "f_ref": f_ref}


def total_energy_damping(fs: int, y: np.ndarray, f_eff: float) -> Dict[str, float]:
    """Оценивает затухание СУММАРНОЙ ЭНЕРГИИ: берем E(t)=y^2(t), сглаживаем огибающую sqrt(E),
    фиттим ln(E) = a + b t, тогда декремент энергии за период T_eff: δ_E = -b / f_eff.
    """
    dt = 1 / fs
    t = np.arange(len(y)) * dt
    E = y ** 2
    # Сгладим E через скользящее среднее на ~полпериода эффективной частоты
    if f_eff and f_eff > 0:
        win = max(int(0.5 * fs / f_eff), 3)
    else:
        win = 101
    kernel = np.ones(win) / win
    E_smooth = np.convolve(E, kernel, mode="same")
    # Фит экспоненты для энергии
    c0, c1 = fit_exponential_decay(t, E_smooth)
    delta_E = max(0.0, -c1 / f_eff) if f_eff and f_eff > 0 else np.nan
    return {"delta_E": delta_E, "slope": c1, "win": win}

# -------------------- ВСПОМОГАТЕЛЬНАЯ ОБЩАЯ ОБРАБОТКА --------------------

def full_analysis(path: str, channel: int = 0, height_frac: float = 0.1, distance_hz: float = 5.0, max_peaks: int = 6,
                  bw_rule: str = "relative", bw_hz: float = 10.0, bw_rel: float = 0.2,
                  show_plots: bool = True, spectrum_xlim: Optional[Tuple[float, float]] = None) -> Dict[str, object]:
    """Полный цикл:
    1) чтение канала
    2) спектр, поиск пиков
    3) выделение гармоник и их метрики (δ, ζ, энергия)
    4) суммарный сигнал и его декремент
    5) суммарная энергия и ее декремент
    Возвращает словарь с результатами и таблицами.
    """
    fs, x = read_wav_channel(path, channel=channel)

    # Спектр и пики
    freqs, amp = compute_spectrum(fs, x)
    peaks_idx = find_harmonic_peaks(freqs, amp, height_frac=height_frac, distance_hz=distance_hz, max_peaks=max_peaks)

    if show_plots:
        plot_raw_signal(fs, x, title=f"Сырой сигнал (канал {channel})")
        plot_spectrum(freqs, amp, title="Спектр (амплитуда)", xlim=spectrum_xlim)
        # отметим пики
        plt.figure(figsize=(11,3))
        plt.semilogy(freqs, amp, label="Спектр")
        if len(peaks_idx):
            plt.semilogy(freqs[peaks_idx], amp[peaks_idx], "rx", label="Пики")
        if spectrum_xlim: plt.xlim(*spectrum_xlim)
        plt.xlabel("Частота, Гц"); plt.ylabel("Амплитуда (лог)")
        plt.title("Пики спектра")
        plt.legend(); plt.tight_layout(); plt.show()

    # Выделение гармоник
    components = decompose_into_harmonics(fs, x, peaks_idx, freqs, amp, bw_rule=bw_rule, bw_hz=bw_hz, bw_rel=bw_rel)

    if show_plots and components:
        plot_harmonics_time(fs, components, max_plots=min(len(components), 6))

    table = components_table(components)

    # Суммарный аппроксимированный сигнал (сумма полосовых компонент)
    y_sum = reconstruct_sum(components)

    # Декремент суммарного сигнала
    total_sig = total_signal_damping(fs, y_sum if len(y_sum) else x, f_ref=None)

    # Эффективная частота и декремент энергии
    f_eff = effective_frequency_by_energy(components) if components else (freqs[np.argmax(amp)] if len(freqs) else np.nan)
    total_en = total_energy_damping(fs, y_sum if len(y_sum) else x, f_eff=f_eff)

    if show_plots and len(y_sum):
        dt = 1 / fs
        t = np.arange(len(y_sum)) * dt
        plt.figure(figsize=(11,3))
        plt.plot(t, y_sum, label="Сумма выделенных гармоник")
        plt.xlabel("Время, с"); plt.ylabel("Амплитуда"); plt.title("Суммарный аппроксимированный сигнал")
        plt.tight_layout(); plt.show()

        # Показать огибающую и ln(огибающей)
        env = analytic_envelope(y_sum)
        plt.figure(figsize=(11,3)); plt.plot(t, env); plt.title("Огибающая суммарного сигнала"); plt.tight_layout(); plt.show()
        ln_env = np.log(env + 1e-12)
        plt.figure(figsize=(11,3)); plt.plot(t, ln_env); plt.title("ln(огибающей) суммарного сигнала"); plt.tight_layout(); plt.show()

        # Энергия во времени
        E = y_sum**2
        plt.figure(figsize=(11,3)); plt.plot(t, E); plt.title("Мгновенная энергия y_sum^2"); plt.tight_layout(); plt.show()

    results = {
        "fs": fs,
        "x": x,
        "freqs": freqs,
        "amp": amp,
        "peaks_idx": peaks_idx,
        "components": components,
        "components_table": table,
        "y_sum": y_sum,
        "total_signal": total_sig,
        "f_eff": f_eff,
        "total_energy": total_en,
    }
    return results

# -------------------- ПРИМЕР ИСПОЛЬЗОВАНИЯ --------------------
if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="WAV Blade Damping Toolkit")
    p.add_argument("path", type=str, help="Путь к WAV файлу")
    p.add_argument("--channel", type=int, default=0, help="Номер канала (0-индексация)")
    p.add_argument("--max_peaks", type=int, default=6, help="Максимум пиков (гармоник) для анализа")
    p.add_argument("--height_frac", type=float, default=0.1, help="Порог по высоте пиков (доля от max)")
    p.add_argument("--distance_hz", type=float, default=5.0, help="Мин. расстояние между пиками (Гц)")
    p.add_argument("--bw_rule", type=str, default="relative", choices=["relative","fixed"], help="Правило полосы фильтра")
    p.add_argument("--bw_hz", type=float, default=10.0, help="Полоса фильтра (если fixed)")
    p.add_argument("--bw_rel", type=float, default=0.2, help="Относительная полоса (если relative)")
    p.add_argument("--no_plots", action="store_true", help="Не показывать графики")
    args = p.parse_args()

    res = full_analysis(
        path=args.path,
        channel=args.channel,
        height_frac=args.height_frac,
        distance_hz=args.distance_hz,
        max_peaks=args.max_peaks,
        bw_rule=args.bw_rule,
        bw_hz=args.bw_hz,
        bw_rel=args.bw_rel,
        show_plots=not args.no_plots,
    )

    # Печать кратких итогов
    print("\nПики (Гц):", np.round(res["freqs"][res["peaks_idx"]], 2) if len(res["peaks_idx"]) else [])
    print("\nТаблица компонент:")
    try:
        print(res["components_table"].to_string(index=False))
    except Exception:
        print(res["components_table"])  # на случай отсутствия pandas display
    print("\nСуммарный сигнал: δ≈{:.4f}, ζ≈{:.4f}, f_ref≈{:.2f} Гц".format(
        res["total_signal"]["delta"], res["total_signal"]["zeta"], res["total_signal"]["f_ref"]))
    print("Суммарная энергия: δ_E≈{:.4f}, f_eff≈{:.2f} Гц (окно {} отсчетов)".format(
        res["total_energy"]["delta_E"], res["f_eff"], res["total_energy"]["win"]))
