import fileio # FIX THIS! Had trouble importing this library ...
import containers # FIX THIS TOO!
import events # AND THIS
import numpy
import MIDI


reasonableNumberOfTicksForaFile = 2**18  # 1365 bars of 4/4
velocityData = numpy.empty((reasonableNumberOfTicksForaFile,128), numpy.int8)
timeOfLastEventForThisNote = numpy.empty(MIDI.Note_Count, numpy.int32)

# Public
def fromMIDIFile(fileName, fCombineTracksAndChannels=True):
    # FIX THIS "fileio" should be "midi" but I couldn't get pip to work.
    tracks = fileio.read_midifile(fileName)

    #make all the timestamps into absolute (rather than relative) tick counts
    for track in tracks:
        track.make_ticks_abs()

    #combine all the tracks into one super-track of events, sorted in tick-order
    if fCombineTracksAndChannels:
        allEvents = [event for track in tracks for event in track]
        allEvents.sort()
    else:
        raise( NotImplementedError("fCombineTracksAndChannels=False"))

    #re-initialize globals
    lastEventTime = 0
    velocityData.fill(0)
    timeOfLastEventForThisNote.fill(0)

    #handle each message
    for event in allEvents:
        if event.statusmsg == MIDI.Message_NoteOn:
            addEvent(event.tick, event.pitch, event.velocity)
        if event.statusmsg == MIDI.Message_NoteOff:
            addEvent(event.tick, event.pitch, 0)

    # What's the python short syntax for this???
    lastTick = allEvents[-1].tick
    newData = numpy.empty((lastTick+1,128), numpy.int8)
    for i in xrange(lastTick):
        for j in xrange(velocityData.shape[1]-1):
            newData[i,j] = velocityData[i,j]
    return newData


def addEvent(tick, note, velocity):
    # make sure our array is big enough
    checkDataLength(velocityData, tick)

    # If the note is already on, mark everything up to one tick before this note
    lastEventTime = timeOfLastEventForThisNote[note]
    currentVelocity = velocityData[lastEventTime, note]
    if currentVelocity > 0:
        for t in xrange(lastEventTime+1, tick-1):
            velocityData[t, note] = currentVelocity

    # if we're re-attacking a note that's already on, add a one-tick gap, to force the synthesizer to restart the sound
    if velocity == 0:
        velocityData[tick-1,note] = currentVelocity
    else:
        velocityData[tick-1,note] = 0

    timeOfLastEventForThisNote[note] = tick
    velocityData[tick, note] = velocity


def checkDataLength(data, newLength):
    if newLength >= data.shape[0]:
        print "Warning: MIDI_reasonableNumberOfTicksForaFile isn't. Increase this constant, please."
        print "New length: {0} Old length:{1}".format(newLength, data.shape[0])

        newData = numpy.empty((newLength + 1024,128), numpy.int8)

        # What's the python short syntax for this???
        for i in xrange(data.shape[0]-1):
            for j in xrange(data.shape[1]-1):
                newData[i,j] = data[i,j]

        velocityData = newData


#Public
def toMIDIFile(data, fileName):

    # FIX THIS "containers" should be "midi" but I couldn't get pip to work.
    tracks = containers.Pattern()
    track  = containers.Track()
    tracks.append(track)

    # Side-effect of this test implementation: all the note events wind up on the same track.

    for note in xrange(MIDI.Note_Count):
        if (data[0, note] > 0):
            # FIX THIS "events" should be "midi" but I couldn't get pip to work.
            msg = events.NoteOnEvent(tick=0, velocity=data[0,note], pitch=note)
            track.append[msg]

    for t in xrange(1,data.shape[0]-1):
        for note in xrange(MIDI.Note_Count):
            if (data[t,note] != data[t-1,note]):
                # FIX THIS "events" should be "midi" but I couldn't get pip to work.
                msg = events.NoteOnEvent(tick=t, velocity=data[t,note], pitch=note)
                track.append[msg]

    endMsg = events.EndOfTrackEvent(data.shape[0])
    track.append(endMsg)

    # FIX THIS "fileio" should be "midi" but I couldn't get pip to work.
    fileio.write_midiFile(fileName, tracks)


