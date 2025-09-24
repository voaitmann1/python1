import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import csv
import os
#
from scipy.signal import find_peaks
from scipy.signal import detrend
from scipy.signal import tukey
import math
from scipy.optimize import curve_fit
#
from scipy.signal import butter, filtfilt, hilbert
import copy
#---

signalFileHeader=["Time_s", "Signal", "Energy"]
fileCharsHeadersRow=["DataID", "FileName", "freq.discr", "tmax", "SumEnergy"]
impactRangesHeadersRow=["tStart", "tFin"]

#

def FindExtremsOfArray(arr):
    if isinstance(arr, list) and len(arr)>0:
        mx=arr[1-1]
        mn=arr[1-1]
        mxN=1
        mnN=1
        for N in range(1, len(arr)+1):
            val=arr[N-1]
            if val>mx:
                mx=val
                mxN=N
            if val<mn:
                mn=val
                mnN=N
    return mnN, mn, mxN, mx

def SwapVals(arr, N1, N2):
    if isinstance(arr, list) and len(arr)>0 and N1>=1 and N1<=len(arr) and N2>=1 and N2<=len(arr):
        val1=arr[N1-1]
        val2=arr[N2-1]
        buf=val1
        arr[N1-1]=arr[N2-1]
        arr[N2-1]=buf
    #return arr#
        
def SortArray(arr, AscNotDesc=True):
    if isinstance(arr, list):
        Q=len(arr)
        buf=0
        if AscNotDesc:
            for i in range(1, Q-1+1):
                for j in range(i, Q+1):
                    if(arr[j-1]<arr[i-1]):
                        buf=copy.deepcopy(arr[i-1])
                        arr[i-1]=copy.deepcopy(arr[j-1])
                        arr[j-1]=copy.deepcopy(buf)
                    #
                #
            #
        else:
            for i in range(1, Q-1+1):
                for j in range(i, Q+1):
                    if(arr[j-1]>arr[i-1]):
                        buf=copy.deepcopy(arr[i-1])
                        arr[i-1]=copy.deepcopy(arr[j-1])
                        arr[j-1]=copy.deepcopy(buf)
                    #
                #
            #
        #
    #return arr

    
#

def read_wav_safe(fullFileName, max_seconds=None):
    try:
        fs, data=wavfile.read(fullFileName)
        #norm'g if data s'numoz
        if np.issubdtype(data.dtype, np.integer):
            max_val= np.iinfo(data.dtype).max
            data=data.astype(np.float32)
        return fs, data
    except Exception as e:
        print("Error reading file "+str(e))
        print("trying to read via wave")
        #with wave.open(fileName, "rb") as wf:#os not l'methods __enter__ et __exit__, so n'arb
        wf=wave.open(fullFileName, "rb")
        fs=wf.getframerate()
        n_channels = wf.getnchannels()
        n_frames = wf.getnframes()

        if max_seconds is not None:
            #data = data.reshape(-1, n_channels)
            n_frames = min(n_frames, int(fs * max_seconds))

        raw = wf.readframes(n_frames)

        wf.close()#ute nur uz py 2.7 ob in py 3 to obj ha attr __exit__
          
        data = np.frombuffer(raw,dtype = np.int16)

        if n_channels >1:
            data = data.reshape(-1, n_channels)
            #print(str(n_channels)+" channels")
        else:
            pass
            #print(str(n_channels)+" channels")

        data = data.astype(np.float32)/ np.iinfo(np.int16).max
        return fs, data

#---

def read_wav_and_calc_t(filename):
    #fs, data = wavfile.read(filename)
    fs, data = read_wav_safe(filename, max_seconds=None)
    if data.ndim > 1:
        data = data[:,0]  # первый канал, если стерео

    t = np.arange(len(data)) / fs
    return t, data, fs
    

def read_wav_and_save_csv(filename):# not used
    #fs, data = wavfile.read(filename)
    fs, data = read_wav_safe(filename, max_seconds=None)
    if data.ndim > 1:
        data = data[:,0]  # первый канал, если стерео

    t = np.arange(len(data)) / fs

    # --- Сохраняем сигнал в CSV ---
    csv_filename = os.path.splitext(filename)[0] + "_signal.csv"
    with open(csv_filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(["Time_s", "Signal"])
        writer.writerow(["Time_s", "Signal", "Energy"])
        for i in range(len(t)):
            #writer.writerow([t[i], data[i]])
            writer.writerow([t[i], data[i], data[i]*data[i]])

    print(f"Сигнал сохранён в {csv_filename}")
    return t, data, fs

def plot_signal(t, signal, title="Сигнал", t_start=None, t_end=None):
    t = np.array(t)
    signal = np.array(signal)
    if t_start is None:
        t_start = t[0]
    if t_end is None:
        t_end = t[-1]

    mask = (t >= t_start) & (t <= t_end)
    plt.figure(figsize=(12,6))
    plt.plot(t[mask], signal[mask])
    plt.xlabel("Время, с")
    plt.ylabel("Амплитуда")
    plt.title(title)
    plt.grid()
    plt.show()

# -----------------------------
def SaveToCsv(csv_filename, headerRow, data2D):
    with open(csv_filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        #writer.writerow(["Time_s", "Signal"])
        writer.writerow(headerRow)
        #for i in range(len(t)):
            #writer.writerow([t[i], data[i]])
        writer.writerows(data2D)
#------------------------------------------------------------
def read_signal_csv(filename):
    times = []
    values = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(float(row["Time_s"]))
            values.append(float(row["Signal"]))
    return np.array(times), np.array(values)

def read_SignalAndEnergy_csv(filename):
    times = []
    signal = []
    energy = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(float(row["Time_s"]))
            signal.append(float(row["Signal"]))
            energy.append(float(row["Energy"]))
    return np.array(times), np.array(signal), np.array(energy)

def read_impact_bounds(filename):
    impacts = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)#all rows
        for row in reader:
            impacts.append((int(row["ImpactID"]), float(row["StartTime_s"]), float(row["EndTime_s"])))
    return impacts

def read_FileChars(filename):
    fileChars = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            fileChars.append((int(row["ImpactID"]), float(row["StartTime_s"]), float(row["EndTime_s"])))
    return fileChars

def ReadDiscretFreq(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)#all rows
        for row in reader:
            fN=int(row[fileCharsHeadersRow[1-1]])
            fnm=row[fileCharsHeadersRow[2-1]]
            fs=float(row[fileCharsHeadersRow[3-1]])
            tm=float(row[fileCharsHeadersRow[4-1]])
            es=float(row[fileCharsHeadersRow[5-1]])
            break
    #return fs
    return fN, fnm, fs, tm, es
#------------------------------------------------------------
def parabolic_interpolation(k, A):
    # k - индекс пика, A - массив амплитуд
    alpha = A[k-1]
    beta  = A[k]
    gamma = A[k+1]
    p = 0.5 * (alpha - gamma) / (alpha - 2*beta + gamma)
    # скорректированная частота:
    k_true = k + p
    amp_true = beta - 0.25*(alpha - gamma)*p
    return k_true, amp_true
#============================================================

#import numpy as np
#from scipy.signal import find_peaks

def detect_impacts_segments(x, fs=1000, min_distance=0.05, threshold_ratio=0.5):
    """
    x - сигнал (список или numpy array)
    fs - частота дискретизации, Гц
    min_distance - минимальное расстояние между ударами, сек
    threshold_ratio - порог амплитуды относительно максимума для пика
    """
    x = np.array(x, dtype=float)
    distance_samples = int(min_distance * fs)
    max_amp = np.max(x)
    threshold = threshold_ratio * max_amp

    # Находим пики ударов
    peaks_idx, _ = find_peaks(x, height=threshold, distance=distance_samples)

    # Переводим в моменты времени
    peaks_time = peaks_idx / fs

    # Формируем сегменты: от одного удара до следующего
    segments = []
    for i in range(len(peaks_time)-1):
        segments.append((peaks_time[i], peaks_time[i+1]))
    # Последний сегмент до конца записи
    segments.append((peaks_time[-1], len(x)/fs))

    return peaks_time, segments

# ----------------------------
# Пример использования
# ----------------------------
if __name__ == "__main__":
    fs = 1000  # Гц
    t = np.arange(0, 1, 1/fs)

    # Пример сигнала: 3 удара (синусоиды с затуханием) + шум
    x = np.zeros_like(t)
    for center in [0.2, 0.5, 0.8]:
        idx_center = int(center*fs)
        N = 50
        decay = np.exp(-np.arange(N)/20)
        x[idx_center:idx_center+N] += 1.0 * decay * np.sin(2*np.pi*50*np.arange(N)/fs)
    x += 0.05 * np.random.randn(len(t))  # шум

    peaks_time, segments = detect_impacts_segments(x, fs, min_distance=0.1, threshold_ratio=0.3)

    print("Моменты ударов (сек):", peaks_time)
    print("Фрагменты между ударами (сек):", segments)

#===============================================================================

#import math
#import numpy as np
#import matplotlib.pyplot as plt

# ----------------------------
# 1. Прямое вычисление ДПФ
# ----------------------------
def spectrum_dft(x, fs=1000, use_window=False, writeProgress=True):

    if writeProgress==True:
        print("spectrum_dft starts working")
    
    N = len(x)
    x_proc = np.array(x, dtype=float)

    # Применяем окно Hann
    if use_window:
        window = np.hanning(N)
        x_proc *= window

    X_real = [0.0] * N
    X_imag = [0.0] * N

    if writeProgress==True:
        print("starting double cycle")

    N1=0
    
    for k in range(N):
        for n in range(N):

            N1+=1
            workPart=N1*100.0/(N*N)
            if writeProgress==True:
                ##if workPart%10==0 or workPart<10 and workPart%2==0 or workPart==0 or workPart==1:
                #if workPart%2==0 or workPart==1:
                #    print(f"Calculating: {workPart}% done")
                print("Calc "+str(workPart)+"% done")
            
            angle = 2 * math.pi * k * n / N
            X_real[k] += x_proc[n] * math.cos(angle)
            X_imag[k] -= x_proc[n] * math.sin(angle)

    amps = [2 * math.sqrt(X_real[k]**2 + X_imag[k]**2) / N for k in range(N//2)]
    freqs = [k * fs / N for k in range(N//2)]

    if writeProgress==True:
        print("spectrum_dft finishes working")
    
    return freqs, amps

# ----------------------------
# 2. Быстрое преобразование FFT
# ----------------------------
def spectrum_fft(x, fs=1000, use_window=False, use_mean=False, use_detrend=False):
    xi=copy.deepcopy(x)

    x_proc = np.array(xi, dtype=float)#or S'n'ute copy, if utf'tc np.array?

    if use_mean:
        x_proc = x_proc - np.mean(x_proc)  # убрать DC

    if use_detrend:    
        x_proc = detrend(x_proc)
    
    N = len(x_proc)

    # Применяем окно Hann
    if use_window:
        window = np.hanning(N)
        x_proc *= window

    X = np.fft.fft(x_proc)
    amps = 2 * np.abs(X[:N//2]) / N
    freqs = np.fft.fftfreq(N, d=1/fs)[:N//2]
    return freqs, amps



# ----------------------------
# 3. Итоговая функция с выбором варианта
# ----------------------------
def compute_spectrum(x, fs=1000, method='fft', use_window=False, plot=True):
    """
    x - сигнал (список или numpy array)
    fs - частота дискретизации
    method - 'fft' или 'dft'
    use_window - применять окно Hann
    plot - строить график
    """
    if method == 'fft':
        freqs, amps = spectrum_fft(x, fs, use_window)
    elif method == 'dft':
        freqs, amps = spectrum_dft(x, fs, use_window)
    else:
        raise ValueError("method must be 'fft' or 'dft'")

    if plot:
        plt.figure(figsize=(8,4))
        plt.plot(freqs, amps)
        plt.xlabel("Частота, Гц")
        plt.ylabel("Амплитуда")
        plt.title(f"Спектр сигнала ({method}, window={use_window})")
        plt.grid(True)
        plt.show()

    return freqs, amps

#======================================================================

# Spectrum lib

#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.signal import find_peaks
#import csv


# ------------------------------
# 1. Расчёт спектра
# ------------------------------
def compute_spectrum(x, fs, use_window=False, use_mean=False, use_detrend=False, zero_padding_factor=1):
    """
    Вычисление спектра сигнала.
    """
    x_proc = np.array(x, dtype=float)

    if use_mean:
        x_proc -= np.mean(x_proc)
    if use_detrend:
        x_proc = detrend(x_proc)

    N_orig = len(x_proc)
    N = N_orig * zero_padding_factor
    if zero_padding_factor > 1:
        x_proc = np.pad(x_proc, (0, N - N_orig), 'constant')

    if use_window:
        window = np.hanning(len(x_proc))
        x_proc *= window

    X = np.fft.fft(x_proc)
    amps = 2 * np.abs(X[:N//2]) / N
    freqs = np.fft.fftfreq(N, d=1/fs)[:N//2]

    return freqs, amps

# ------------------------------
# 2. Поиск пиков в спектре
# ------------------------------
def find_spectrum_peaks(freqs, amps, min_height=None, min_prominence=None,
                        min_distance_hz=None, peak_thresh=None,
                        to_console=False, to_csv=None):
    """
    Поиск пиков спектра с возможностью гибкой настройки параметров.
    """
    df = freqs[1] - freqs[0]
    distance_pts = int(np.ceil(min_distance_hz / df)) if min_distance_hz else None

    if peak_thresh is not None:
        min_height = peak_thresh * np.max(amps)

    peaks, props = find_peaks(
        amps,
        height=min_height,
        prominence=min_prominence,
        distance=distance_pts
    )

    peak_freqs = freqs[peaks]
    peak_vals = amps[peaks]

    if to_console:
        print("Найденные пики:")
        for f, v in zip(peak_freqs, peak_vals):
            print(f"  {f:.2f} Гц : {v:.4f}")

    if to_csv:
        with open(to_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Frequency_Hz", "Amplitude"])
            writer.writerows(zip(peak_freqs, peak_vals))

    return peak_freqs, peak_vals, peaks

# ------------------------------
# 3. Вывод спектра
# ------------------------------
def plot_spectrum(freqs, amps, peak_freqs=None, peak_vals=None, title="Spectrum"):
    plt.figure(figsize=(10,5))
    plt.plot(freqs, amps, label='Spectrum')
    if peak_freqs is not None and peak_vals is not None:
        plt.plot(peak_freqs, peak_vals, 'ro', label='Peaks')
    plt.xlabel("Frequency, Hz")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

# ------------------------------
# 4. Выделение мод
# ------------------------------
def extract_modes_from_spectrum(t, signal, fs, peaks_csv, save_dir="modes", bandwidth=1.0, use_window=False):
    """
    Выделение отдельных мод по спектру, используя CSV с пиками.
    """
    os.makedirs(save_dir, exist_ok=True)

    # Считываем пики
    peak_freqs = []
    with open(peaks_csv, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # заголовок
        for row in reader:
            peak_freqs.append(float(row[0]))

    N = len(signal)
    if use_window:
        signal_proc = signal * np.hanning(N)
    else:
        signal_proc = np.array(signal, dtype=float)

    spectrum = np.fft.fft(signal_proc)
    freqs = np.fft.fftfreq(N, d=1/fs)

    modes = {}
    for f0 in peak_freqs:
        mask = (np.abs(freqs - f0) <= bandwidth/2) | (np.abs(freqs + f0) <= bandwidth/2)
        spectrum_filt = spectrum * mask
        sig_filt = np.fft.ifft(spectrum_filt).real
        modes[f0] = sig_filt

        # Сохраняем в CSV
        csv_file = os.path.join(save_dir, f"mode_{f0:.2f}Hz.csv")
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Time_s", "Signal"])
            writer.writerows(zip(t, sig_filt))
        print(f"[+] Мода {f0:.2f} Гц сохранена → {csv_file}")

    return modes

def extract_realistic_modes(signal, t, fs, peak_freqs, bandwidth=1.0):
    """
    Выделение мод с сохранением реального затухания.
    
    signal     : массив исходного сигнала
    t          : массив времени
    fs         : частота дискретизации
    peak_freqs : массив пиковых частот
    bandwidth  : ширина полосы вокруг каждого пика
    """
    N = len(signal)
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, d=1/fs)
    
    # Огибающая сигнала
    analytic_signal = hilbert(signal)
    envelope = np.abs(analytic_signal)
    
    # Найдем момент максимума огибающей
    idx_max = np.argmax(envelope)
    
    modes = {}
    
    for f0 in peak_freqs:
        # маска полосы вокруг пика
        mask = (np.abs(freqs - f0) <= bandwidth/2) | (np.abs(freqs + f0) <= bandwidth/2)
        filtered_spec = spectrum * mask
        mode_signal = np.fft.ifft(filtered_spec).real
        
        # масштабирование амплитуды моды
        factor = envelope[idx_max] / (mode_signal[idx_max] + 1e-12)  # чтобы избежать деления на 0
        mode_signal *= factor
        
        modes[f0] = mode_signal
        
    return modes, envelope


# 1. Функция построения огибающей
def compute_envelope(signal):
    """
    Вычисляет огибающую сигнала через Hilbert
    """
    analytic_signal = hilbert(signal)
    envelope = np.abs(analytic_signal)
    return envelope

# 2. Функция спектра
def compute_spectrum(signal, fs=1000, use_window=False):
    """
    Вычисление спектра сигнала
    """
    N = len(signal)
    x_proc = np.array(signal, dtype=float)
    
    if use_window:
        window = np.hanning(N)
        x_proc *= window

    X = np.fft.fft(x_proc)
    freqs = np.fft.fftfreq(N, d=1/fs)[:N//2]
    amps = 2 * np.abs(X[:N//2]) / N
    return freqs, amps

# 3. Поиск пиков спектра с параметрами регулировки
def find_spectrum_peaks(freqs, amps,
                        min_height=None,
                        min_prominence=None,
                        min_distance_hz=None):
    """
    Автоматический поиск пиков спектра с порогами и минимальной дистанцией
    """
    df = freqs[1] - freqs[0]  # шаг по частоте
    min_distance_pts = int(np.ceil(min_distance_hz / df)) if min_distance_hz else None

    peaks, props = find_peaks(
        amps,
        height=min_height,
        prominence=min_prominence,
        distance=min_distance_pts
    )

    peak_freqs = freqs[peaks]
    peak_vals = amps[peaks]

    return peak_freqs, peak_vals, peaks

# 4. Выделение реалистичных мод
def extract_realistic_modes(signal, t, fs, peak_freqs, envelope=None, bandwidth=1.0):
    """
    Выделение мод с реалистичным убывающим затуханием
    """
    N = len(signal)
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(N, d=1/fs)
    
    if envelope is None:
        envelope = compute_envelope(signal)
    idx_max = np.argmax(envelope)
    
    modes = {}
    for f0 in peak_freqs:
        mask = (np.abs(freqs - f0) <= bandwidth/2) | (np.abs(freqs + f0) <= bandwidth/2)
        filtered_spec = spectrum * mask
        mode_signal = np.fft.ifft(filtered_spec).real
        
        # Масштабирование моды по огибающей
        factor = envelope[idx_max] / (mode_signal[idx_max] + 1e-12)
        mode_signal *= factor
        
        modes[f0] = mode_signal
        
    return modes

# 5. Визуализация спектра с пиками
def plot_spectrum_with_peaks(freqs, amps, peak_freqs=None, peak_vals=None):
    plt.figure(figsize=(10,5))
    plt.plot(freqs, amps, label="Спектр")
    if peak_freqs is not None and peak_vals is not None:
        plt.plot(peak_freqs, peak_vals, 'ro', label="Пики")
    plt.xlabel("Частота, Гц")
    plt.ylabel("Амплитуда")
    plt.title("Спектр с выделенными пиками")
    plt.grid(True)
    plt.legend()
    plt.show()

#======================================================================

#from scipy.signal import hilbert, find_peaks
#from scipy.optimize import curve_fit


def analyze_signal(t, x, method="hilbert"):
    """
    Вычисление огибающей и логарифмического декремента затухания.
    method: 'hilbert', 'mnk_lib', 'mnk_manual'
    """
    t = np.asarray(t)
    x = np.asarray(x)

    # --- метод Гильберта ---
    if method == "hilbert":
        analytic = hilbert(x)
        envelope = np.abs(analytic)

    # --- МНК библиотечный ---
    elif method == "mnk_lib":
        def exp_decay(t, A0, delta):
            return A0 * np.exp(-delta * t)

        peaks, _ = find_peaks(np.abs(x))
        t_peaks = t[peaks]
        x_peaks = np.abs(x[peaks])

        if len(t_peaks) < 2:
            return np.abs(x), None

        params, _ = curve_fit(exp_decay, t_peaks - t_peaks[0], x_peaks, p0=(x_peaks[0], 1.0))
        A0_fit, delta_fit = params
        envelope = exp_decay(t - t_peaks[0], A0_fit, delta_fit)

    # --- МНК ручной ---
    elif method == "mnk_manual":
        peaks, _ = find_peaks(np.abs(x))
        t_peaks = t[peaks]
        x_peaks = np.abs(x[peaks])

        if len(t_peaks) < 2:
            return np.abs(x), None

        # линейная регрессия: ln(A) = ln(A0) - delta * t
        t_rel = t_peaks - t_peaks[0]
        y = np.log(x_peaks + 1e-8)
        coeffs = np.polyfit(t_rel, y, 1)
        slope, intercept = coeffs
        delta_fit = -slope
        envelope = np.exp(intercept) * np.exp(-delta_fit * (t - t_peaks[0]))

    else:
        raise ValueError("method должен быть 'hilbert', 'mnk_lib' или 'mnk_manual'")

    # --- оценка δ через линейную регрессию по ln(огибающей) ---
    log_env = np.log(envelope + 1e-8)
    coeffs = np.polyfit(t - t[0], log_env, 1)
    delta = -coeffs[0]

    return envelope, delta

def plot_several(signals, labels=None, title="Сигналы"):
    #def plot_signals(signals, labels=None, title="Сигналы"):
    """
    signals: список сигналов
      - (t, x) → рисуем в отдельном подграфике
      - ((t1,x1), (t2,x2)) → рисуем вместе с twinx
    labels: список подписей (по желанию)
    """
    if labels is None:
        labels = [f"Signal {i+1}" for i in range(len(signals))]

    n = len(signals)
    fig, axes = plt.subplots(n, 1, figsize=(10, 4*n), squeeze=False)
    axes = axes.ravel()

    for i, sig in enumerate(signals):
        ax = axes[i]

        # один сигнал
        if isinstance(sig[0], (list, np.ndarray)):
            t, x = sig
            ax.plot(t, x, label=labels[i], color="b")
            ax.set_ylabel(labels[i])
            ax.legend(loc="upper right")
            ax.grid(True)

        # пара сигналов (с twinx)
        else:
            (t1, x1), (t2, x2) = sig
            ax.plot(t1, x1, "b", label=labels[i] + " (L)")
            ax.set_ylabel(labels[i] + " (L)")
            ax2 = ax.twinx()
            ax2.plot(t2, x2, "r", label=labels[i] + " (R)")
            ax2.set_ylabel(labels[i] + " (R)")
            ax.grid(True)

        ax.set_xlabel("Time, s")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def plot_several1(data_groups, labels=None, styles=None, title="Signals"):
    """
    Универсальный вывод сигналов.
    
    data_groups: список элементов вида:
        [
            [
                [(x1, t1), (x2, t2), ...],   # сигналы (x,t)
                mode                         # 1 или 2
            ],
            ...
        ]
    
    Если mode == 2 и ровно 2 сигнала → второй рисуется на twinx.
    
    labels: список списков:
        [
            ["xlabel", "ylabel"],                   # для 1-го графика
            ["xlabel", "ylabel", "ylabel_right"],   # если есть twinx
            ...
        ]
    
    styles: список списков стилей:
        [
            [ {"color":"red"}, {"color":"blue"} ],
            ...
        ]
    
    title: общий заголовок окна.
    """

    fig, axes = plt.subplots(len(data_groups), 1, figsize=(10, 4 * len(data_groups)))
    if len(data_groups) == 1:
        axes = [axes]  # для унификации

    for i, (signals, mode) in enumerate(data_groups):
        ax = axes[i]
        lbls = labels[i] if labels and i < len(labels) else []
        stls = styles[i] if styles and i < len(styles) else []

        # подписи осей
        if len(lbls) >= 1: ax.set_xlabel(lbls[0])
        if len(lbls) >= 2: ax.set_ylabel(lbls[1])

        if mode == 2 and len(signals) == 2:
            # первый сигнал - обычный
            #x1, t1 = signals[0]
            t1, x1 = signals[0]
            stl1 = stls[0] if len(stls) >= 1 else {}
            ax.plot(t1, x1, label=lbls[1] if len(lbls) >= 2 else None, **stl1)

            # второй сигнал - twinx
            #x2, t2 = signals[1]
            t2, x2 = signals[1]
            stl2 = stls[1] if len(stls) >= 2 else {}
            ax2 = ax.twinx()
            if len(lbls) >= 3: ax2.set_ylabel(lbls[2])
            ax2.plot(t2, x2, label=lbls[2] if len(lbls) >= 3 else None, **stl2)
        else:
            # несколько сигналов в одной системе координат
            for j, (t, x) in enumerate(signals):
                #for j, (x, t) in enumerate(signals):
                stl = stls[j] if j < len(stls) else {}
                lbl = lbls[j+1] if len(lbls) > j+1 else None
                ax.plot(t, x, label=lbl, **stl)

        if len(lbls) > 1:
            ax.legend()

    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

#from scipy.signal import tukey

def analyze_signal1(t, x, method="hilbert", n_peaks=8, peak_thresh=0.1, window_alpha=0.1):
    """
    Вычисление огибающей и логарифмического декремента затухания.
    
    method: 'hilbert', 'mnk_lib', 'mnk_manual'
    n_peaks: сколько первых пиков брать для МНК
    peak_thresh: относительный порог (доля от max), ниже которого пики игнорируются
    window_alpha: параметр окна Tukey для Гильберта (0 = прямоугольное, 1 = Хэннинга)
    """
    t = np.asarray(t)
    x = np.asarray(x)

    # --- метод Гильберта ---
    if method == "hilbert":
        win = tukey(len(x), alpha=window_alpha) if window_alpha > 0 else np.ones(len(x))
        x_win = x * win
        analytic = hilbert(x_win)
        envelope = np.abs(analytic)

    # --- МНК библиотечный ---
        #x_proc = x_proc - np.mean(x_proc)  # убрать DC
        #x_proc = detrend(x_proc)#local variable 'x_proc' referenced before assignment
        x_proc=copy.deepcopy(x)
        x_proc = x_proc - np.mean(x_proc)  # убрать DC
        x_proc = detrend(x_proc)#
    elif method == "mnk_lib":
        def exp_decay(t_rel, A0, delta):
            return A0 * np.exp(-delta * t_rel)

        peaks, props = find_peaks(np.abs(x), height=peak_thresh * np.max(np.abs(x)))
        t_peaks = t[peaks]
        x_peaks = np.abs(x[peaks])

        if len(t_peaks) < 2:
            return np.abs(x), None

        # ограничиваем числом первых пиков
        t_peaks, x_peaks = t_peaks[:n_peaks], x_peaks[:n_peaks]

        params, _ = curve_fit(exp_decay, t_peaks - t_peaks[0], x_peaks, p0=(x_peaks[0], 1.0))
        A0_fit, delta_fit = params
        envelope = exp_decay(t - t_peaks[0], A0_fit, delta_fit)

    # --- МНК ручной ---
    elif method == "mnk_manual":
        peaks, props = find_peaks(np.abs(x), height=peak_thresh * np.max(np.abs(x)))
        t_peaks = t[peaks]
        x_peaks = np.abs(x[peaks])

        if len(t_peaks) < 2:
            return np.abs(x), None

        # ограничиваем числом первых пиков
        t_peaks, x_peaks = t_peaks[:n_peaks], x_peaks[:n_peaks]

        # линейная регрессия: ln(A) = ln(A0) - delta * t
        t_rel = t_peaks - t_peaks[0]
        y = np.log(x_peaks + 1e-8)
        slope, intercept = np.polyfit(t_rel, y, 1)
        delta_fit = -slope
        envelope = np.exp(intercept) * np.exp(-delta_fit * (t - t_peaks[0]))
    elif method == "mytry":
        pass
    else:
        raise ValueError("method должен быть 'hilbert', 'mnk_lib' или 'mnk_manual'")

    # --- оценка δ через регрессию по огибающей ---
    log_env = np.log(envelope + 1e-8)
    slope, intercept = np.polyfit(t - t[0], log_env, 1)
    delta = -slope

    return envelope, delta

#============================================================================

def extract_modes_and_save(t, signal, fs, save_dir="results",
                           bandwidth=1.0, peak_thresh=0.05):
    """
    Извлекает отдельные моды колебаний из сигнала по спектру и сохраняет в CSV.

    t          – массив времени
    signal     – сигнал
    fs         – частота дискретизации
    save_dir   – папка для сохранения результатов
    bandwidth  – ширина полосы вокруг пика (Гц)
    peak_thresh– относительный порог для поиска пиков в спектре
    """

    # FFT
    N = len(signal)
    freqs = np.fft.fftfreq(N, d=1/fs)
    spectrum = np.fft.fft(signal)
    amps = np.abs(spectrum) / N

    # Только положительные частоты
    mask_pos = freqs > 0
    freqs_pos, amps_pos = freqs[mask_pos], amps[mask_pos]

    # Поиск пиков
    peak_inds, props = find_peaks(amps_pos, height=peak_thresh * np.max(amps_pos))
    peak_freqs = freqs_pos[peak_inds]

    # Создать папку для результатов
    os.makedirs(save_dir, exist_ok=True)

    modes = {}
    for f0 in peak_freqs:
        mask = (np.abs(freqs - f0) <= bandwidth/2) | (np.abs(freqs + f0) <= bandwidth/2)
        spectrum_filt = spectrum * mask
        sig_filt = np.fft.ifft(spectrum_filt).real
        modes[f0] = sig_filt

        # --- сохраняем в CSV ---
        csv_filename = os.path.join(save_dir, f"mode_{f0:.2f}Hz.csv")
        with open(csv_filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time_s", "Signal"])
            for ti, si in zip(t, sig_filt):
                writer.writerow([ti, si])
        print(f"[+] Сохранён отклик {f0:.2f} Гц → {csv_filename}")

    return peak_freqs, modes

## ===== пример использования =====
#if __name__ == "__main__":
#    # Примерные данные
#    fs = 1000  # Гц
#    t = np.linspace(0, 5, fs*5, endpoint=False)
#    signal = (np.sin(2*np.pi*3*t) + 0.5*np.sin(2*np.pi*7*t))*np.exp(-t/2) + 0.05*np.random.randn(len(t))
#
#    # Извлекаем моды
#    peaks, modes = extract_modes_and_save(t, signal, fs,
#                                          save_dir="modes_results",
#                                          bandwidth=2.0,
#                                          peak_thresh=0.1)
#
#    # Визуализация
#    plt.figure(figsize=(10,6))
#    for f, sig_f in modes.items():
#        plt.plot(t, sig_f, label=f"{f:.1f} Hz")
#    plt.plot(t, signal, "k--", alpha=0.4, label="Исходный")
#    plt.legend()
#    plt.xlabel("Время, с")
#    plt.ylabel("Амплитуда")
#    plt.title("Выделенные моды колебаний")
#    plt.grid(True)
#    plt.show()
#


#==============================================================================
    
def MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, vsh=0):
    #QPoints=125#f'tei
    #QSects=10#100#f'tei
    #QPoints=len(signal)
    QPairs=QPoints-1
    #dt=1/fs
    SectLenMed=QPairs/QSects
    SectLenInt=int(QPairs/QSects)
    rest=QPairs%QSects
    if vsh>0:
        print("QPoints="+str(QPoints)+" QSects="+str(QSects)+" QPairs="+str(QPairs)+" SectLenInt="+str(SectLenInt)+" SectLenMed="+str(SectLenMed)+" rest="+str(rest)+" In all: "+str(SectLenInt*QSects+rest))
        print("Forming rows")
    rows=[]
    row=[]
    rowN=0
    for N in range (1, QPoints+1):
        if vsh==1 or vsh==3:
            print("N="+str(N))
        row.append(N)
        if N%QSects==0:
            if N<SectLenInt*QSects:
                if vsh==1 or vsh==3:
                    print("row bound reached")
                    print("row:")
                    print(row)
                #rowToAdd=copy.deepcopy(row)
                #rows.append(rowToAdd)
                rows.append(row)
                rowN+=1
                if vsh==1 or vsh==3:
                    print("latest subRow")
                    print(rows[rowN-1])
                if rowN>2:
                    if vsh==1 or vsh==3:
                        print("pre-latest subRow")
                        print(rows[rowN-2])
                row=[]
                #rowToAdd=[]
                row.append(N)
                #print("row bound reached")
            else:
                print("N="+str(N)+"=SectLenInt*QSects="+str(SectLenInt)+"*"+str(QSects)+"="+str(SectLenInt*QSects)+" - ignoring this point")
        elif N==QPoints:
            if vsh==1 or vsh==3:
                print("end reached")
                print("row:")
                print(row)
            #rowToAdd=copy.deepcopy(row)
            #rows.append(rowToAdd)
            rows.append(row)
            rowN+=1
            if vsh==1 or vsh==3:
                print("last subRow")
                print(rows[rowN-1])
            if rowN>2:
                if vsh==1 or vsh==3:
                    print("pre-last subRow")
                    print(rows[rowN-2])
            #rowToAdd=[]
            row=[]
            break
        #
    #
    if vsh==2 or vsh==3:
        QRows=len(rows)
        print("Result - "+str(QRows)+" rows:")
        for rowN in range(1, QRows+1):
            rowL=len(rows[rowN-1])
            print("row"+str(rowN)+" L="+str(rowL))
            for cmpnN in range(1, rowL-1+1):
                print(str(rows[rowN-1][cmpnN-1])+" ... "+str(rows[rowN-1][cmpnN-1+1]))
    #
    return rows
#

def MyEnvelopeBuilding_part2of3_IntegrOrMean(signal, QSects, fs=1):
    dt=1/fs
    rowsSs=[]
    rowsHs=[]
    QPoints=len(signal)
    rowsOfNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects)
    QRows=len(rowsOfNs)
    if fs==1:
        for rowN in range(1, QRows+1):
            rowL=len(rowsOfNs[rowN-1])
            rowS=0
            for i in range(1, rowL-1+1):
                N1=rowsOfNs[rowN-1][i-1]
                N2=rowsOfNs[rowN-1][i+1-1]
                rowS+=(signal[N1-1]+signal[N2-1])/2
            rowsSs.append(rowS)#je s'mult'd by 1, so S'S. Div S to (Q-1) = S/b=h
            rowsHs.append(rowS/(rowL-1))
    else:
        for rowN in range(1, QRows+1):
            rowL=len(rowsOfNs[rowN-1])
            rowS=0
            for i in range(1, rowL-1+1):
                N1=rowsOfNs[rowN-1][i-1]
                N2=rowsOfNs[rowN-1][i+1-1]
                rowS+=(signal[N1-1]+signal[N2-1])/2
            rowsSs.append(rowS*dt)#je s'mult'd by 1, so S'S. Div S to (Q-1) = S/b=h
            rowsHs.append(rowS/((rowL-1)*dt))
    return rowsHs

def MyEnvelopeBuilding_part2of3_SortMax(signal, QSects, percent=33, vsh=1):
    Maxs=[]
    NLast=0
    QPoints=len(signal)
    if vsh!=0:
        print("MyEnvelopeBuilding_part2of3_SortMax starts working")
    rowsOfNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, vsh=0)
    QRows=len(rowsOfNs)
    for i in range(1, QRows+1):
        rowIni=[]
        rowL=len(rowsOfNs[i-1])
        RowFirstN=rowsOfNs[i-1][1-1]
        RowLastN=rowsOfNs[i-1][rowL-1]
        for j in range(RowFirstN, RowLastN+1):
            val=signal[j-1]
            rowIni.append(val)
        if vsh!=0:
            print("rowN"+str(i))
            print("row initial")
            print(rowIni)
        rowSorted=[]
        rowSorted=copy.deepcopy(rowIni)
        SortArray(rowSorted, False)
        if vsh!=0:
            print("row sorted")
            print(rowSorted)
        rowSelected=[]
        for j in range(1, rowL-1+1):
            if j/rowL<=percent/100 and (j+1)/rowL>percent/100:
                NLast=j
                break
        rowSelected=rowSorted[0:NLast+1]
        if vsh!=0:
            print("row selected")
            print(rowSelected)
        s=0
        for  j in range(1, NLast+1):
            s+=rowSelected[j-1]
        Maxs.append(s/NLast)
    if vsh!=0:
        print("Finally:")
        print(Maxs)
        print("MyEnvelopeBuilding_part2of3_SortMax finishes working")
    return Maxs

def MyEnvelopeBuilding_part2of3_FindMax(signal, QSects, percent=33, vsh=0):
    Maxs=[]
    NLast=0
    QPoints=len(signal)
    if vsh!=0:
        print("MyEnvelopeBuilding_part2of3_SortMax starts working")
    rowsOfNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, vsh=0)
    QRows=len(rowsOfNs)
    for i in range(1, QRows+1):
        rowIni=[]
        rowL=len(rowsOfNs[i-1])
        RowFirstN=rowsOfNs[i-1][1-1]
        RowLastN=rowsOfNs[i-1][rowL-1]
        for j in range(RowFirstN, RowLastN+1):
            val=signal[j-1]
            rowIni.append(val)
        if vsh!=0:
            print("rowN"+str(i))
            print("row initial")
            print(rowIni)
        #rowSorted=[]
        #rowSorted=copy.deepcopy(rowIni)
        #SortArray(rowSorted, False)
        #if vsh!=0:
        #    print("row sorted")
        #    print(rowSorted)
        #rowSelected=[]
        #for j in range(1, rowL-1+1):
        #    if j/rowL<=percent/100 and (j+1)/rowL>percent/100:
        #        NLast=j
        #        break
        #rowSelected=rowSorted[0:NLast+1]
        #if vsh!=0:
        #    print("row selected")
        #    print(rowSelected)
        #s=0
        #for  j in range(1, NLast+1):
        #    s+=rowSelected[j-1]
        #Maxs.append(s/NLast)
        mnN, mn, mxN, mx = FindExtremsOfArray(rowIni)
        Maxs.append(mx)
    if vsh!=0:
        print("Finally:")
        print(Maxs)
        print("MyEnvelopeBuilding_part2of3_SortMax finishes working")
    return Maxs
        


def MyEnvelopeBuilding_part3of3_BuildingStairs(signal, QSects, fs=1, vrnN_Integr1_SortedMaxs2_Max3=2, percent=33, vsh=0):
    QPoints=len(signal)
    rowsOfNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, 0)
    if vrnN_Integr1_SortedMaxs2_Max3==1:
        rowsHs=MyEnvelopeBuilding_part2of3_IntegrOrMean(signal, QSects, fs)
    elif vrnN_Integr1_SortedMaxs2_Max3==2:
        rowsHs=MyEnvelopeBuilding_part2of3_SortMax(signal, QSects, percent=1, vsh=vsh)#33
    elif vrnN_Integr1_SortedMaxs2_Max3==3:
        rowsHs=MyEnvelopeBuilding_part2of3_FindMax(signal, QSects)
    QRows=len(rowsOfNs)
    Hs=[]
    n=0
    for i in range(1, QRows+1):
        rowL=len(rowsOfNs[i-1])
        val=rowsHs[i-1]
        for j in range(1, rowL-1+1):
            n+=1
            Hs.append(val)
            if(vsh==1):
                print("Pt "+str(n)+" rowN="+str(i)+" N in row="+str(j)+" row lims: ("+str(rowsOfNs[i-1][1-1])+"..."+str(rowsOfNs[i-1][rowL-1])+") val="+str(val)+"="+str(Hs[n-1]))
    n+=1
    Hs.append(val)
    if(vsh==1):
        print("Pt "+str(n)+" rowN="+str(i)+" N in row="+str(j)+" row lims: ("+str(rowsOfNs[i-1][1-1])+"..."+str(rowsOfNs[i-1][rowL-1])+") val="+str(val)+"="+str(Hs[n-1]))
    return Hs

def MyEnvelopeBuilding_part4of3_BuildingCurve_NurInitialT(signal, QSects, fs=1, vrnN_Integr1_SortedMaxs2_Max3=3, percent=1, vsh=0):
    QPoints=len(signal)
    rowsOfNs=MyEnvelopeBuilding_part1of3_SortPointsNumbersToSects_to2DArr(QPoints, QSects, 0)
    if vrnN_Integr1_SortedMaxs2_Max3==1:
        rowsHs=MyEnvelopeBuilding_part2of3_IntegrOrMean(signal, QSects, fs)
    elif vrnN_Integr1_SortedMaxs2_Max3==2:
        rowsHs=MyEnvelopeBuilding_part2of3_SortMax(signal, QSects, percent=1, vsh=vsh)#33
    elif vrnN_Integr1_SortedMaxs2_Max3==3:
        rowsHs=MyEnvelopeBuilding_part2of3_FindMax(signal, QSects)
    QRows=len(rowsOfNs)
    trs=[]
    #trf=[]
    MeanX=0
    MeanY=0
    for i in range(QRows):
        L=len(rowsOfNs[i])
        trs.append(rowsOfNs[i][1-1])
        #    trf.append(rowsOfNs[i][L-1])
        MeanX+=rowsOfNs[i][1-1]
        MeanY+=rowsHs[i]
    #return trs, trf, rowsHs
    MeanX/=QRows
    MeanY/=QRows
    numerator=0
    m1=0
    m2=0
    denominator=0
    for i in range(QRows):
       m1= trs[i] - MeanX
       m2= rowsHs[i] - MeanY
       numerator+=(m1*m2)
       denominator+=(m1*m1)
    beta=numerator/denominator
    alfa = MeanY - beta*MeanX
    return alfa, beta
