# Arpeggiator
This project is an arpeggiator in Max/MSP developed in collaboration with guitarist Ben Levin. It was originally developed to be used with 6-string guitar equipped with a Fishman TriplePlay pick-up but if you dive into the code and understand the inner working it could be easily adapted to any MIDI device. A demo of an early version can be seen at https://www.youtube.com/watch?v=F8_mWvoNuPo

The latest code version can be found: Arpeggiator/Advanced Arpeggiator/v0.5/

The idea behind the project was to an arpeggio and map its various parameters to the bend signal provided by the MIDI pick-up. For instance you could change the rate of arpeggiation, the voicing of the arpeggio, the notes enabled in the arpeggio, etc... It's configured to use the lowest two strings (MIDI channels 5 and 6) to select the root as well as tonality (limited only to the major scale modes at the moment). For example to set the key to G Major you would play a major third across the E and A strings starting on the 3rd fret. To go to C Dorian you would play a major sixth on the 8th fret of the E string and 12th fret of the A string. Each of the different modes uses an interval corresponding the the unique tone that differentiates it from the other modes (see RootAndTonalityController.maxpat for more info)

From a technical standpoint the project was a success but the results turned out to be less musical than hoped for. It did however provide a chance to explore the interesting territory of how to represent tonality on a computer.
