# MusicToolsForNupic

## Dependecies

This depends on github/olemb/mido

## VelocityData

Use from MIDIVelocityData import *

**LoadVelocityDataFromMIDIFilee** ( _fileName_ ) read the MIDI file _fileName_ and return a numpy array _d_ = [_length_ _of_ _piece_ _in_ _ticks_ X MIDI.Note_Count] where:     

If note _n_ is playing at time _t_, then d[_t_,_n_] is the velocity used when the note began.

If note _n_ is not playing at time _t_, then d[_t_,_n_] is zero.
    
A note _n_ begins at time _t_ if d[_t_,_n_] > d[_t_-1,_n_]

A note _n_ ends at time _t_ if d[_t_-1,_n_] > 0 and d[_t_,_n_] = 0

This is the "piano roll" representation of a musical piece.
    
**SaveVelocityDataToMIDIFile** ( _data_, _fileName_ ) creates a MIDI file using the data.

## Music

Contains constants describing **notes**, **octaves** and **pitch classes**, and these utility functions:

**Music.pitchClass** ( _note_ )

**Music.octave** ( _note_ )

**Music.noteFromOctaveAndPitchClass** ( _octave_, _pitchClass_ )

**Music.pitchInHz** ( _note_ )

**Music,noteName ( _note_ )

**Music.intervalClassicalConsonance** ( _note1_, _note2_ ) Consonance as it is taught to elementary music theory students, with four possible values: Music.dissonance, Music.consonant, Music.perfectConsonance, Music.unison

## MIDI

Contains constants from the general MIDI standard for messages, notes, controllers and so on.


  
