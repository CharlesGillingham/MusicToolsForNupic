from mido import MidiTrack, MetaMessage

def merge_tracksFIXED(tracks):
    """Returns a MidiTrack object with all messages from all tracks.

    The messages are returned in playback order with delta times
    as if they were all in one track.
    """
    now = 0 # REMOVE THIS
    messages = MidiTrack()
    for track in tracks:
        now = 0 # ADD THIS
        for message in track:
            now += message.time
            if message.type not in ('track_name', 'end_of_track'):
                messages.append(message.copy(time=now))
            if message.type == 'end_of_track':
                break

    messages.sort(key=lambda x: x.time)
    messages.append(MetaMessage('end_of_track', time=now))

    # Convert absolute time back to delta time.
    last_time = 0
    for message in messages:
        message.time -= last_time
        last_time += message.time

    return messages
