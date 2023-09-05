import mido
from mido import MidiFile, MidiTrack, Message

# Define a dictionary to map MIDI note numbers to Solresol syllables.
midi_to_solresol = {
    60: 'do',
    62: 're',
    64: 'mi',
    65: 'fa',
    67: 'sol',
    69: 'la',
    71: 'si',
}

def get_arturia_port():
    for name in mido.get_input_names():
        if 'Arturia MiniLab mkII' in name:
            return name
    return None

def midi_to_solresol_note(midi_note):
    return midi_to_solresol.get(midi_note, '')

def main():
    port_name = get_arturia_port()

    if port_name is None:
        print("Arturia MiniLab mkII not found.")
        return

    with mido.open_input(port_name) as inport:
        print(f"Listening to {port_name}... Press keys on your MIDI keyboard.")
        for msg in inport:
            if msg.type == 'note_on':
                note = midi_to_solresol_note(msg.note)
                if note:
                    print(f"MIDI Note: {msg.note}, Solresol: {note}")

if __name__ == '__main__':
    main()


