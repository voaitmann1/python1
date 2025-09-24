import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def read_wav(filename):
    """
    Читает WAV-файл.
    Возвращает: частота дискретизации fs (Гц), массив данных data (numpy.ndarray).
    Если сигнал многоканальный, то data.shape = (N, num_channels).
    """
    fs, data = wavfile.read(filename)
    # нормализация: если данные целочисленные (int16), переведём в float [-1, 1]
    if np.issubdtype(data.dtype, np.integer):
        max_val = np.iinfo(data.dtype).max
        data = data.astype(np.float32) / max_val
    return fs, data

def plot_signal(data, fs, channel=0, duration=None):
    """
    Строит график выбранного канала.
    channel: индекс канала (0 - первый, 1 - второй и т.д.)
    duration: ограничение по времени (секунды), если None — рисует весь сигнал
    """
    if data.ndim == 1:
        y = data
    else:
        y = data[:, channel]

    t = np.arange(len(y)) / fs
    if duration:
        mask = t < duration
        t = t[mask]
        y = y[mask]

    plt.figure(figsize=(10,4))
    plt.plot(t, y, linewidth=0.8)
    plt.xlabel("Время, с")
    plt.ylabel("Амплитуда")
    plt.title(f"Сигнал (канал {channel})")
    plt.grid(True)
    plt.show()

#

fs, data = read_wav("test.wav")   # загружаем wav
plot_signal(data, fs, channel=0, duration=2.0)
