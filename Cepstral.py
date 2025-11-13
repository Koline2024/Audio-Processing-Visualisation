import librosa
import librosa.feature
import matplotlib.pyplot as plt
import numpy as np

class Processing:
    def __init__(self, wavInput, wavKey):
        self.wavInput = wavInput
        self.wavKey = wavKey
        #Load the audio with librosa
        try:
            self.yInput, self.srInput = librosa.load(wavInput, sr = None)
            self.yKey, self.srKey = librosa.load(wavKey, sr = None)
        except FileNotFoundError:
            print("Files not found!")
        #Compute MFCCs
        self.mfccInput = librosa.feature.mfcc(y = self.yInput, sr = self.srInput, n_mfcc = 13)
        self.mfccKey = librosa.feature.mfcc(y = self.yKey, sr = self.srKey, n_mfcc = 13)

    def plotMFCCs(self):
        fig, ax = plt.subplots(1, 2, figsize=(14, 10))
        #Input
        ax[0].librosa.display.specshow(self.mfccInput, x_axis="time", sr=self.srInput)
        ax[0].colorbar(format="%+2.0f dB")
        ax[0].title("MFCC Input")
        ax[0].ylabel("MFCC Coefficient")
        ax[0].xlabel("Time (s)")

        #Key
        ax[1].librosa.display.specshow(self.mfccKey, x_axis="time", sr=self.srKey)
        ax[1].colorbar(format="%+2.0f dB")
        ax[1].title("MFCC Input")
        ax[1].ylabel("MFCC Coefficient")
        ax[1].xlabel("Time (s)")

        plt.subplots_adjust(wspace = 0.3)
        plt.subplots_adjust(hspace = 0.3)
        plt.show()



