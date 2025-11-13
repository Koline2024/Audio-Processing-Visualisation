import FFTAnalysis
import Cepstral

def main():
    wavInput = "WavFiles/Chris.wav"
    wavKey = "WavFiles/Peter.wav"
    wavAnalyse = Cepstral.Processing(wavInput, wavKey)
    wavAnalyse.preProcess()
    print(wavAnalyse.compareMFCCs())
    wavAnalyse.plotMFCCs()

if __name__ == "__main__":
    main()



