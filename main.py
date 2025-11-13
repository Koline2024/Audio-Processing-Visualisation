import FFTAnalysis
import Cepstral

def main():
    wavInput = "WavFiles/Saunders Hall 3.wav"
    wavKey = "WavFiles/Saunders Hall 4.wav"
    wavAnalyse = Cepstral.Processing(wavInput, wavKey)
    print(wavAnalyse.compareMFCCs())
    wavAnalyse.plotMFCCs()

if __name__ == "__main__":
    main()



