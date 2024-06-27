import numpy as np
import matplotlib.pyplot as plt
from math import pi

def sinus():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    return y
def obliczDFT():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    N = len(y)
    n = np.arange(0, N)
    dft = np.dot(y, np.exp(-2j * pi * (n * n.reshape((N, 1)) / N)))
    return dft
def obliczFFT():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    N = len(y)
    n = np.arange(0, N)
    fft = np.fft.fft(y, np.exp(-2j * pi * (n * n.reshape((N, 1)) / N)))
    return fft
def printDft():
    sinuss = sinus()
    N = len(sinuss)
    fs = N * 2
    freq = np.arange(0, fs, fs / N)
    plt.plot(freq, np.abs(obliczDFT()))
    plt.title("Widmo")
    plt.xlabel("Częstotliwoc")
    plt.ylabel("Amplituda")
    plt.xlim(0, fs / 2)
    plt.show()
printDft()
