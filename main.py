import Utilities

def main():
    wavName = 'WavFiles/html5bytebeat.wav'
    wavAnalyse = Utilities.Processing(wavName)
    wavAnalyse.plotWav()

if __name__ == "__main__":
    main()



