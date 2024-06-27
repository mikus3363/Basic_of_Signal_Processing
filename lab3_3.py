import numpy as np
import time

def dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)

Fs = 1000
T = 1/Fs
t = np.arange(0, 1, T)

frequency = 100
signal = np.sin(2 * np.pi * frequency * t)

#dla DFT
start_time_dft = time.perf_counter()
dft_result = dft(signal)
end_time_dft = time.perf_counter()
dft_time = end_time_dft - start_time_dft

#dla FFT
start_time_fft = time.perf_counter()
fft_result = np.fft.fft(signal)
end_time_fft = time.perf_counter()
fft_time = end_time_fft - start_time_fft

print(f'Czas wykonania DFT: {dft_time} sekundy')
print(f'Czas wykonania FFT: {fft_time} sekundy')