import mido
import itertools

class TrackPlayer:

    def __init__(self, track):
        self.iterator = iter(track)
        self.ticks = 0
        self.done = False
        self.next_message = None
    
    def step(self, n = 1):
        self.ticks -= n

    def messages(self):
        if self.ticks <= 0 and not self.done:
            if self.next_message:
                yield self.next_message
            try:
                self.next_message = next(self.iterator)
                self.ticks += self.next_message.time
                yield from self.messages()
            except StopIteration:
                self.done = True



def translate(in_file):
    mid = mido.MidiFile(in_file)

    players = [TrackPlayer(track) for track in mid.tracks]
    output_stages = []

    # default BPM for MIDI; meta messages can change it later
    output_stages.append('!speed@120')

    while not all(p.done for p in players):
        # don't bother discriminating between tracks
        # for now

        for message in itertools.chain.from_iterable(
                p.messages() for p in players
            ):
            if message.type == 'note_on':
                pitch = message.note - 69 # assuming the base is 'concert a'
                # volume = message.velocity / 64
                # output_stages.append(f'!volume@{100 * volume}')
                output_stages.append(f'stopposting@{pitch}')
                output_stages.append('!combine')
            elif message.type == 'note_off' and False:
                output_stages.append('!cut')
            elif message.type == 'set_tempo':
                bpm = mido.tempo2bpm(message.tempo)
                output_stages.append(f'!speed@{bpm}')
        
        step = min((p.ticks for p in players if not p.done), default=0)
        beats = step / mid.ticks_per_beat
        output_stages.append(f'!stop@{beats}')

        for p in players:
            p.step(step)
    
    return '|'.join(output_stages)

