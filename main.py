import Utilities

def main():
    wavInput = "WavFiles/html5bytebeat.wav"
    wavKey = "WavFiles/audiocheck.net_sin_0.5Hz_-3dBFS_3s.wav"
    wavAnalyse = Utilities.Processing(wavInput, wavKey)
    wavAnalyse.plotWav()

if __name__ == "__main__":
    main()



