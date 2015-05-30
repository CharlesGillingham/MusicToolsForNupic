from mido import MidiFile, MidiTrack, Message
import numpy

from MIDOBUGFIX import merge_tracksFIXED

MIDINotes = xrange(128)
_reasonableNumberOfTicksForaFile = 2**18  # 1365 bars of 4/4

# A local persistant array to avoid re-allocating giant arrays all the time.
_velocityData = numpy.empty((_reasonableNumberOfTicksForaFile,len(MIDINotes)), numpy.int8)
_timeOfLastEventForThisNote = numpy.empty(len(MIDINotes), numpy.int32)
_velocityData.fill(0)
_timeOfLastEventForThisNote.fill(0)



# Public
def LoadVelocityDatafromMIDIFile(fileName):
    """Create and return a new velocity data array.

    """
    global _velocityData, _timeOfLastEventForThisNote

    mFile = MidiFile(fileName)

    # Merge all the tracks
    allEvents = merge_tracksFIXED(mFile.tracks)

    #handle each message
    t = 0
    eventCount = 0 # DEBUG

    for event in allEvents:
        if event.time < 0: break; # I have seen a negative time for the final message

        # translate the relative time into an absolute time
        t = t + event.time


        if event.type == "note_on":

            # lower the resolution to 24 ticks per beat.
            # e.g., files may have something like 480 ticks per beat, but this much precision isn't necessary for our purposes:
            # we only want to consider "musical" events that occur at rhythmic points in the file. Messages like pitch bend,
            # expression and volume would need to be sampled at a at higher rate.
            t24 = int(round(float(24*t)/ mFile.ticks_per_beat))

            _addEvent(t24, event.note, event.velocity)

            eventCount = eventCount+1 # DEBUG

        elif event.type == "note_off":
            t24 = int(round(float(24*t)/ mFile.ticks_per_beat))
            _addEvent(t24, event.note, 0)
            eventCount = eventCount+1 # DEBUG
        else:
            pass # ignore any other messages

    # Create newData with the right dimensions and return it
    lastTick = t24

    #TODO: pythonize this loop
    newData = numpy.empty((lastTick+24,len(MIDINotes)), numpy.int8)
    for i in xrange(lastTick):
        for j in xrange(_velocityData.shape[1]-1):
            newData[i,j] = _velocityData[i,j]

    # reset the globals to their initial state
    _velocityData.fill(0)
    _timeOfLastEventForThisNote.fill(0)

    print("MIDI File was loaded. Events: {} Time of Last Event: {} Data dimensions: {}".format(eventCount, lastTick, newData.shape))

    return newData



def _addEvent(tick, note, velocity):
    global _velocityData, _timeOfLastEventForThisNote

    # make sure our array is big enough
    _checkDataLength(tick)

    # If the note is already on, mark everything up to one tick before this note
    lastEventTime = _timeOfLastEventForThisNote[note]

    currentVelocity = _velocityData[lastEventTime, note]

    # SPECIAL CASE: There two messages in one tick; this is the second message. This is an unusual case (it probably represents
    # a grace note or some other ornamentation; it's probably not a melodic note event.)
    # More than two messages in a tick is not supported.
    if tick == lastEventTime:
        if velocity == 0:
            if currentVelocity > 0:
                # We are turning a note on and then off in one tick; add a one-tick gap, to force the synthesizer
                # to restart the sound.
                _velocityData[tick-2, note] = 0
                _velocityData[tick-1, note] = currentVelocity
        else:
            if currentVelocity > 0:
                # Two notes start in the same tick; we need two one-tick gaps
                _velocityData[tick-3, note] = 0
                _velocityData[tick-2, note] = currentVelocity
                _velocityData[tick-1, note] = 0
            else:
                # Turning a note off and then on in one tick; we need a one-tick gap just before the note.
                _velocityData[tick-1, note] = 0

    else:

        # NORMAL CASE: If the note is currently on, fill all the space up to this tick
        if currentVelocity > 0:
            for t in xrange(lastEventTime+1, tick):
                _velocityData[t, note] = currentVelocity

        # Another special case: if we're re-attacking a note that's already on, add a one-tick gap, to force the
        # synthesizer to restart the sound.
        if currentVelocity > 0 and velocity > 0:
            _velocityData[tick-1,note] = 0

    _timeOfLastEventForThisNote[note] = tick
    _velocityData[tick, note] = velocity


def _checkDataLength(newLength):
    global _velocityData
    if newLength >= _velocityData.shape[0]:
        print "Warning: _reasonableNumberOfTicksForaFile isn't."
        print "New length: {0} Old length:{1}".format(newLength, velocityData.shape[0])

        newData = numpy.empty((newLength + 1024,128), numpy.int8)

        #TODO: pythonize this loop
        for i in xrange(_velocityData.shape[0]-1):
            for j in xrange(_velocityData.shape[1]-1):
                newData[i,j] = _velocityData[i,j]

        _velocityData = newData
        print "Updated length: {}".format(_velocityData.shape[0])



def SaveVelocityDatatoMIDIFile(vData, fileName):

    with MidiFile(ticks_per_beat = 24) as mFile:
        track = MidiTrack()
        mFile.tracks.append(track)

        for n in MIDINotes:
            if (vData[0,n]>0):
                event = Message("note_on", velocity=int(vData[0,n]), note = int(n), time = int(0))
                track.append(event)

        timeOfLastEvent = 0

        for t in range(1,vData.shape[0]-1):
            for n in MIDINotes:
                if vData[t,n] != vData[t-1,n]:
                    relativeTick = t - timeOfLastEvent
                    timeOfLastEvent = t
                    event = Message("note_on", velocity=int(vData[t,n]), note = int(n), time = int(relativeTick))
                    track.append(event)

        mFile.save(fileName)
        print("MIDI file was saved.  Events: {} Length in ticks: {} Data dimensions: {}".format(len(track), timeOfLastEvent, vData.shape))


