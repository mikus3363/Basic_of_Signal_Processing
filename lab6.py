import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
T = 1/Fs
t = np.arange(0, 1, T)

frequencies = [50,150,200,250] #częstotliwości
signal = np.sin(2 * np.pi * frequencies[0] * t) + np.sin(2 * np.pi * frequencies[1] * t) + np.sin(2 * np.pi * frequencies[2] * t)+ np.sin(2 * np.pi * frequencies[3] * t)

plt.subplot(3, 1, 1) #podział okienka na kilka podrysunków (ile będzie,co ile,miejsce tego)
plt.plot(t, signal)
plt.title('Sygnał sinusoidalny złożony')

#FFT
plt.subplot(3, 1, 2)
fft_res = np.fft.fft(signal)
freq_fft = np.fft.fftfreq(len(fft_res), T)
plt.plot(freq_fft, np.abs(fft_res))
plt.title('FFT sygnału')

plt.subplot(3, 1, 3)
plt.specgram(signal, Fs=Fs)
plt.title('Spektrogram sygnału')


plt.tight_layout()
plt.show()
