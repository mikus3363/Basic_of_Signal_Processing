import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter


# Treść zadania: dla sygnału złożonego z 3 sinusów zastosować filtr DOLNOPRZEPUSTOWY, wyświetlić FFT przed i po filtrze
def generacjSygnalu(fs, duration, frequencies, amplitudes):
    t = np.linspace(0, duration, int(fs * duration))
    signal = np.sum([amp * np.sin(2 * np.pi * freq * t) for freq, amp in zip(frequencies, amplitudes)], axis=0)
    return t, signal


#Po filtrze
def filterDolnoprzepustowyButter(data, cutoff_freq, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff)
    y = lfilter(b, a, data)
    return y


def fft_plot(t, signal, fs, label):
    n = len(signal)
    k = np.arange(n)
    T = n / fs
    frq = k / T
    frq = frq[:n // 2]

    fft_vals = np.fft.fft(signal)
    fft_vals = fft_vals[:n // 2]
    fft_vals = np.abs(fft_vals / n)

    plt.figure()
    plt.plot(frq, fft_vals)
    plt.title(f'FFT {label}')
    plt.xlabel('Częstotliwość (Hz)')
    plt.ylabel('Amplituda')
    plt.show()

#Dane
fs = 1000
duration = 1
frequencies = [50, 150, 450] #częstotliwość
amplitudes = [1, 1, 0.2] #amplitudy

t, signal = generacjSygnalu(fs, duration, frequencies, amplitudes)

#podanie sygnału przed filtrem i wyświetlenie
fft_plot(t, signal, fs, 'Przed filtracją dolnoprzepustową')

cutoff_frequency = 100

#nałożony Filter
filtered_signal = filterDolnoprzepustowyButter(signal, cutoff_frequency, fs)

#podanie sygnału po filtrze i wyświetlenie
fft_plot(t, filtered_signal, fs, 'Po filtracji dolnoprzepustowej')

# Wyświetlenie sygnałów
plt.figure()
plt.plot(t, signal)
plt.plot(t, filtered_signal,label = 'Sygnał po filtracji dolnoprzepustowej')
plt.title('Sygnał przed i po filtracji dolnoprzepustowej')
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda')
plt.legend()
plt.show()
