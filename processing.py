import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

xSignalField = np.linspace(0, 4*np.pi, num = 256)
ySignal = np.sin(xSignalField) + 2*np.sin(xSignalField * 4) + 5*np.sin(xSignalField * 10)
yAmp = fft(ySignal)



plt.plot(xSignalField, yAmp)
plt.show()