import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
import wave

class Processing:
    def __init__(self, wavInput, wavKey):
        self.wavInput = wavInput
        self.wavKey = wavKey
        # wave.open reads the wave file.
        try:
            self.obj = wave.open(self.wavInput, 'rb')
        except FileNotFoundError:
            print("Input wave does not exist.")
        try:
            self.objKey = wave.open(self.wavKey, 'rb')
        except FileNotFoundError:
            print("Key wave does not exist.")
        # sampling frequency
        self.wavFreq = self.obj.getframerate()
        self.wavFreqKey = self.objKey.getframerate()
        # total samples
        self.nSamples = self.obj.getnframes()
        self.nSamplesKey = self.objKey.getnframes()
        # read the whole signal (-1)
        self.wavSignal = self.obj.readframes(-1)
        self.wavSignalKey = self.objKey.readframes(-1)
        # audio clip time is total samples divided by
        # how many samples was taken per second
        self.time = self.nSamples / self.wavFreq
        self.timeKey = self.nSamplesKey / self.wavFreqKey
        # create an array of amplitude values
        self.signalArray = np.frombuffer(self.wavSignal, dtype=np.int16)
        self.signalArrayKey = np.frombuffer(self.wavSignalKey, dtype=np.int16)
        # FFT the signal
        self.fftMagnitude = fft(self.signalArray)
        self.fftFrequency = np.fft.fftfreq(len(self.signalArray), 1 / self.wavFreq)
        self.fftMagnitudeKey = fft(self.signalArrayKey)
        self.fftFrequencyKey = np.fft.fftfreq(len(self.signalArrayKey), 1 / self.wavFreqKey)
        # create an array of equally spaced nums from 0 to time
        self.xAxis = np.linspace(0, self.time, num = self.nSamples)
        self.xAxisKey = np.linspace(0, self.timeKey, num = self.nSamplesKey)
        self.obj.close()
        self.objKey.close()

    """
    plotWav plots the both the original waveform in the time domain
    and the FFT of the waveform in the frequency domain. 
    """
    def plotWav(self):
        # make a subplot to show both graphs at once
        fig, ax = plt.subplots(2, 2, figsize=(14, 10))

        # for time domain (Input)
        ax[0, 0].plot(self.xAxis, self.signalArray)
        ax[0, 0].set_title("Time domain Input")
        ax[0, 0].set_xlabel("Time (s)")
        ax[0, 0].set_ylabel("Amplitude")
        ax[0, 0].grid(True)

        # for freq domain (Input)
        ax[0, 1].plot(np.abs(self.fftFrequency), np.abs(self.fftMagnitude))
        ax[0, 1].set_title("FFT Input")
        ax[0, 1].set_xlabel("Frequency (Hz)")
        ax[0, 1].set_ylabel("Magnitude")
        ax[0, 1].grid(True)

        # for time domain (Key)
        ax[1, 0].plot(self.xAxisKey, self.signalArrayKey)
        ax[1, 0].set_title("Time domain Key")
        ax[1, 0].set_xlabel("Time (s)")
        ax[1, 0].set_ylabel("Amplitude")
        ax[1, 0].grid(True)

        # for freq domain (Key)
        ax[1, 1].plot(np.abs(self.fftFrequencyKey), np.abs(self.fftMagnitudeKey))
        ax[1, 1].set_title("FFT Key")
        ax[1, 1].set_xlabel("Frequency (Hz)")
        ax[1, 1].set_ylabel("Magnitude")
        ax[1, 1].grid(True)


        plt.subplots_adjust(wspace = 0.3)
        plt.subplots_adjust(hspace = 0.3)
        plt.show()

    def compareWav(self):
        return 1
