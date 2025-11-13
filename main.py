import FFTAnalysis

def main():
    wavInput = "WavFiles/quothello-therequot-158832.mp3"
    wavKey = "WavFiles/quothello-therequot-158832.mp3"
    wavAnalyse = FFTAnalysis.Processing(wavInput, wavKey)
    print(wavAnalyse.compareWav())
    wavAnalyse.plotWav()

if __name__ == "__main__":
    main()



