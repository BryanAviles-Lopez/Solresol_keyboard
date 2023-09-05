import mido
from mido import MidiFile, MidiTrack, Message

def get_arturia_port():
    for name in mido.get_input_names():
        if 'Arturia MiniLab mkII' in name:
            return name
    return None

def main():
    port_name = get_arturia_port()

    if port_name is None:
        print("Arturia MiniLab mkII not found.")
        return

    with mido.open_input(port_name) as inport:
        print(f"Listening to {port_name}... Press keys on your MIDI keyboard.")
        for msg in inport:
            print(msg)

if __name__ == '__main__':
    main()

