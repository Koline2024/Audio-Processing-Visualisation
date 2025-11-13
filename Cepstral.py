import librosa
import librosa.feature
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, sosfiltfilt

class Processing:
    def __init__(self, wavInput, wavKey):
        self.wavInput = wavInput
        self.wavKey = wavKey
        self.filteredInput = []
        self.filteredKey = []
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
        imgInput = librosa.display.specshow(self.mfccInput, x_axis = 'time', sr = self.srInput, ax=ax[0])
        fig.colorbar(imgInput, ax = ax[0], format = "%+2.0f dB")
        ax[0].set_title("MFCC Input")
        ax[0].set_ylabel("MFCC Coefficient")
        ax[0].set_xlabel("Time (s)")

        #Key
        imgKey = librosa.display.specshow(self.mfccKey, x_axis="time", sr=self.srKey, ax=ax[1])
        fig.colorbar(imgKey, ax = ax[1], format = "%+2.0f dB")
        ax[1].set_title("MFCC Keyword")
        ax[1].set_ylabel("MFCC Coefficient")
        ax[1].set_xlabel("Time (s)")

        plt.subplots_adjust(wspace = 0.3)
        plt.show()

    def compareMFCCs(self):
        #Use dynamic time warping

        D, wp = librosa.sequence.dtw(X=self.mfccInput, Y=self.mfccKey, metric = 'cosine')
        distance = D[-1, -1]
        similarity = 1 - (distance / np.max(D))
        return similarity

    def preProcess(self):
        #Butterworth Filter below
        nyqInput = 0.5 * self.srInput
        nyqKey = 0.5 * self.srKey
        lowInput = 20 / nyqInput
        lowKey = 20 / nyqKey
        highKey = 20000 / nyqKey
        highInput = 20000 / nyqInput

        highInput = min(highInput, 0.9999)
        highKey = min(highKey, 0.9999)

        sosInput = butter(6, [lowInput, highInput], btype="band", output="sos")
        sosKey = butter(6, [lowKey, highKey], btype="band", output="sos")
        self.filteredInput = sosfiltfilt(sosInput, self.yInput)
        self.filteredKey = sosfiltfilt(sosKey, self.yKey)

        # Compute MFCCs
        self.mfccInput = librosa.feature.mfcc(y=self.filteredInput, sr=self.srInput, n_mfcc=13)
        self.mfccKey = librosa.feature.mfcc(y=self.filteredKey, sr=self.srKey, n_mfcc=13)

