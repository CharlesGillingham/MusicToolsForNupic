from MIDIVelocityData import *


MIDIFilesOnThisMachine = ['/Users/charlesgillingham/Desktop/Music Project -- File/MIDI files/bach_846.mid',
                          '/Users/charlesgillingham/Desktop/Music Project -- File/MIDI files/bach_847.mid',
                          '/Users/charlesgillingham/Desktop/Music Project -- File/MIDI files/bach_850.mid']

FilesToOverwrite = ['/Users/charlesgillingham/Desktop/bach_846_copied.mid',
                    '/Users/charlesgillingham/Desktop/bach_847_copied.mid',
                    '/Users/charlesgillingham/Desktop/bach_850_copied.mid']


for i in xrange(3):
    vd = LoadVelocityDatafromMIDIFile(MIDIFilesOnThisMachine[i])
    SaveVelocityDatatoMIDIFile(vd, FilesToOverwrite[i])
    vd2 = LoadVelocityDatafromMIDIFile(FilesToOverwrite[i])
    assert(vd.shape == vd2.shape)

    for t in range(max(vd.shape[0],vd2.shape[0])):
        for n in MIDINotes:
            if t < vd.shape[0] and t < vd2.shape[0]:
                if not (vd[t,n] == vd2[t,n]):
                    print("vd[{},{}] == {}, vd2[{},{}] == {}".format(t,n,vd[t,n],t,n,vd2[t,n]))
            elif t < vd.shape[0]:
                if vd[t,n] > 0:
                    print("vd[{},{}] == {}, vd2[{},{}] == Missing".format(t,n,vd[t,n],t,n))
            elif t < vd2.shape[0]:
                if vd2[t,n] > 0:
                    print("vd[{},{}] == MISSING, vd2[{},{}] == Missing".format(t,n,t,n,vd2[t,n]))

    #Trying to find this bug ...
    #errorNote = 62
    #errorTime = 4150
    #for t in xrange(errorTime-24, errorTime+24):
    #    arrow = "   "
    #    if t == 4150: arrow = ">>>"
    #    print("{} {} {} {}".format(arrow, t,vd[t,errorNote-12:errorNote+12],vd2[t,errorNote-12:errorNote+12]))




