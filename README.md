## Audio Processing Visualisation ##
This is a repository for my audio processing project. 
In this project, I am attempting to build a word recognition device that 
* Reliably detects a single keyword and differentiates it from other words
* Runs at reasonable speeds on a microcontroller (STM32-Nucleo)
* Can perform a task after input is received
For the first part of the project I will write a proof-of-concept in Python that can reliably detect a keyword, based on Librosa. (Complete)
For the second part of the project I will breadboard the microphone and amplifier circuit and rewrite the Python code to be microcontroller friendly through CMSIS-DSP. (In progress)
For the final part of the project I will finalise the design and create on a PCB with KiCAD.
