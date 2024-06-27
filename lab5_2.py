import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.io import wavfile


file = 'mono.wav'
f, data = wavfile.read(file)

#Postać czasowa:
duration = len(data) / f #ile ma trwać
time = np.linspace(0., duration, len(data))

#Wyświetlenie postaci czasowej
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(time, data)
plt.title('Przebieg czasu')
plt.xlabel('Czas (s)')
plt.ylabel('Amplituda')


#FFT:
n = len(data)
freq = np.fft.fftfreq(n,1/f)
fft_values = fft(data)
fft_data = np.abs(fft_values) / n


# Wyświetlanie postaci FFT
plt.subplot(2, 1, 2)
plt.plot(freq, fft_data)
plt.title('postać FFT')
plt.xlabel('Częstotliwość (Hz)')
plt.ylabel('Amplituda')

plt.tight_layout()
plt.show()
