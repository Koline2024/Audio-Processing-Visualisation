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
        vecInput = self.mfccInput.flatten()
        vecKey = self.mfccKey.flatten()
        #Truncate to the smallest length
        minLength = min(len(vecInput), len(vecKey))
        vecInput = vecInput[:minLength]
        vecKey = vecKey[:minLength]

        #Cosine similarity
        diffRatio = np.dot(vecInput, vecKey) / (np.linalg.norm(vecInput) * np.linalg.norm(vecKey))
        return diffRatio

