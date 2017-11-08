# Arpeggiator
This project is an arpeggiator in Max/MSP developed in collaboration with guitarist Ben Levin. It was originally developed to be used with 6-string guitar equipped with a Fishman TriplePlay pick-up but if you dive into the code and understand the inner working it could be easily adapted to any MIDI device. A demo of an early version can be seen at https://www.youtube.com/watch?v=F8_mWvoNuPo

The latest code version can be found: Arpeggiator/Advanced Arpeggiator/v0.5/

The idea behind the project was to an arpeggio and map its various parameters to the bend signal provided by the MIDI pick-up. For instance you could change the rate of arpeggiation, the voicing of the arpeggio, the notes enabled in the arpeggio, etc. More info about how to use it can be found in the patch itself.

From a technical standpoint the project was a success but the results turned out to be less musical than hoped for. It did however provide a chance to explore the interesting territory of how to represent tonality on a computer.

The patch was originally written in Max 6 and hasn't been tested with Max 7 yet.

There is a dependency on VJ Manzo's Modal Object Library. http://www.vjmanzo.com/mol/
