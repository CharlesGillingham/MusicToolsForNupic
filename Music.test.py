from Music import *

assert(octave(Note_C0) == 0)
assert(octave(Note_MiddleC) == 4)
assert(octave(Note_C7) == 7)
assert(noteFromOctaveAndPitchClass(0, PitchClass_C) == Note_C0)
assert(noteFromOctaveAndPitchClass(4, PitchClass_C) == Note_MiddleC)
assert(noteFromOctaveAndPitchClass(7, PitchClass_C) == Note_C7)

for oct in xrange(-2,8):
    for pc in pitchClasses:
        note = noteFromOctaveAndPitchClass(oct, pc)
        assert(pitchClass(note) == pc)
        assert(octave(note) == oct)

for pc1 in pitchClasses:
    for pc2 in pitchClasses:
        consonance = intervalClassicalConsonance(pc1,pc2)
        assert(consonance in classicalConsonances)

        # Consonance is the same in all octaves
        for oct1 in xrange(0,7):
            for oct2 in xrange(0,7):
                n1 = noteFromOctaveAndPitchClass(oct1,pc1)
                n2 = noteFromOctaveAndPitchClass(oct2,pc2)
                assert(consonance == intervalClassicalConsonance(n1,n2))
