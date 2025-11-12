import Utilities

def main():
    wavInput = "WavFiles/audiocheck.net_50Hz_-5dBFS_25Hz_-17dBFS_3s.wav"
    wavKey = "WavFiles/audiocheck.net_sin_50Hz_-3dBFS_3s.wav"
    wavAnalyse = Utilities.Processing(wavInput, wavKey)
    print(wavAnalyse.compareWav())
    #wavAnalyse.plotWav()

if __name__ == "__main__":
    main()



