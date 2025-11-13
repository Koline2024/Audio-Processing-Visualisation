import Cepstral

def main():
    wavInput = "WavFiles/Shoe.wav"
    wavKey = "WavFiles/Flew.wav"
    wavAnalyse = Cepstral.Processing(wavInput, wavKey)
    wavAnalyse.preProcess()
    print(wavAnalyse.compareMFCCs())
    wavAnalyse.plotMFCCs()

if __name__ == "__main__":
    main()


