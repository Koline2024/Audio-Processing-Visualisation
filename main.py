import matplotlib.pyplot as plt
import numpy as np
import wave, sys

wavName = 'audiocheck.net_sin_0.5Hz_-3dBFS_3s.wav'
obj = wave.open(wavName, 'rb')
wavFreq = obj.getframerate()
nSamples = obj.getnframes()
wavSignal = obj.readframes(-1)
time = nSamples / wavFreq
signalArray = np.frombuffer(wavSignal, dtype = np.int16)

xAxis = np.linspace(0, time, num=nSamples)
plt.figure(figsize=(15, 5))
plt.plot(xAxis, signalArray)
plt.title('Audio Plot')
plt.ylabel(' signal wave')
plt.xlabel('time (s)')
plt.xlim(0, time) #limiting the x axis to the audio time
plt.show()



