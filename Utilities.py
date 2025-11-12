import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
import wave

class Processing:
    def __init__(self, wavName):
        self.wavName = wavName

    def plotWav(self):
        # wave.open reads the wave file.
        obj = wave.open(self.wavName, 'rb')
        # sampling frequency
        wavFreq = obj.getframerate()
        # total samples
        nSamples = obj.getnframes()
        # read the whole signal (-1)
        wavSignal = obj.readframes(-1)
        # audio clip time is total samples divided by
        # how many samples was taken per second
        time = nSamples / wavFreq
        # create an array of amplitude values
        signalArray = np.frombuffer(wavSignal, dtype=np.int16)
        # FFT the signal
        fftMagnitude = fft(signalArray)
        fftFrequency = np.fft.fftfreq(len(signalArray), 1 / wavFreq)
        # create an array of equally spaced nums from 0 to time
        xAxis = np.linspace(0, time, num=nSamples)
        # make a subplot to show both graphs at once
        fig, ax = plt.subplots(1, 2, figsize=(14, 5))

        # for time domain
        ax[0].plot(xAxis, signalArray)
        ax[0].set_title("Time domain signal")
        ax[0].set_xlabel("Time (s)")
        ax[0].set_ylabel("Amplitude")
        ax[0].grid(True)

        # for freq domain
        ax[1].plot(fftFrequency, np.abs(fftMagnitude))
        ax[1].set_title("FFT")
        ax[1].set_xlabel("Frequency (Hz)")
        ax[1].set_ylabel("Magnitude")
        ax[1].grid(True)

        plt.subplots_adjust(wspace=0.3)
        plt.show()

