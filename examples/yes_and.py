
# yes, and? by Ariana Grande
@highest_range
def chord_stabs():
    if notes_hit_x("o--xo--xo-x-o-x-o", sixteenth_notes):
        play(voice_lead_notes(), release=0.125)

def drums():
    if is_quarter_note:
        play(BASS_DRUM)
    if notes_hit_x("-x-x", quarter_notes):
        play(HAND_CLAP)

@low_range
def bass():
    if notes_hit_x("x---x--xx-x---x", sixteenth_notes):
        play(root)

chorus = (('D#m', 4), ('G#7', 4))
verse = (('A#7', 4), ('A#', 4))

PARTS = [
    [chorus*2, [chord_stabs, drums, bass]],
    [verse*2, [chord_stabs,  drums, bass]] 
]
  
BPM = 119
    