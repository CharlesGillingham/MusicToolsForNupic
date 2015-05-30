from math import floor

# Music.Note is aligned with MIDI, except that Music doesn't assume notes are limited to 0..127
Note_C0      = 12
Note_A440    = 57
Note_MiddleC = 60 # C4
Note_C7      = 96

Octave_0      = 0
Octave_Middle = 4
Octave_7      = 7

pitchClasses = xrange(12)

PitchClass_C          =  0
PitchClass_Csharp     =  1
PitchClass_Dflat      =  1
PitchClass_D          =  2
PitchClass_Dsharp     =  3
PitchClass_Eflat      =  3
PitchClass_E          =  4
PitchClass_F          =  5
PitchClass_Fsharp     =  6
PitchClass_Gflat      =  7
PitchClass_G          =  7
PitchClass_Gsharp     =  7
PitchClass_Aflat      =  8
PitchClass_A          =  9
PitchClass_Asharp     = 10
PitchClass_Bflat      = 10
PitchClass_B          = 11


def pitchClass( note ):
    if (note >= 0):
        return note % 12
    else:
        return (11 - ((-note-1) % 12))

def octave( note ):
    if (note >= 0):
        return int(floor(note/12))-1
    else:
        return -(int(floor((-note-1)/12)))-2

def noteFromOctaveAndPitchClass( octave=4, pitchClass=0  ):
    return (octave+1)*12 + pitchClass

def pitchInHz ( note ):
    return (440*2^(((note) - Note_A440)/12));


dissonant         = 0
consonant         = 1
perfectConsonance = 2
unison            = 3
classicalConsonances = xrange(dissonant,unison+1)

def intervalClassicalConsonance( note1, note2 ):
    interval = abs(note2 - note1) % 12
    return {0: unison,            # Unison
            1: dissonant,
            2: dissonant,         # 2nd
            3: consonant,
            4: consonant,         # 3rd
            5: perfectConsonance, # 4th
            6: dissonant,
            7: perfectConsonance, # 5th
            8: consonant,
            9: consonant,         # 6th
            10:dissonant,
            11:dissonant          # 7th
            }[interval]


# A complete version would consider the key signature

PitchClassNames = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]

PitchClassNameDictionary = {"C":0, "C#":1, "D":2, "Eb":3, "E":4, "F":5, "F#":6, "G":7, "Ab":8, "A":9, "Bb":10, "B":11}

def noteName( note ):
    return "{}{}".format(PitchClassNames[pitchClass(note)],octave(note))

#TODO: PORT THIS FROM CMusic
