
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2.0, 0.01) # od x ,do x ,roznica ciagu
y = np.sin(2.0*np.pi*x) # cykl*pi*x

plt.xlabel("os x") #nazwa dla x
plt.ylabel("os y") #nazwa dla y
plt.title("wykres sinusa") #nazwa wykresu
plt.grid(True) #siatka

plt.plot(x,y)
plt.show()
