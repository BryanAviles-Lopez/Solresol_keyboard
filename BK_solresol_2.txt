import mido
from mido.midifiles import MidiMessage
import time

# Define dictionaries for MIDI to Solresol and Solresol to English translations
midi_to_solresol = {
    60: 'do', 62: 're', 64: 'mi', 65: 'fa', 67: 'sol', 69: 'la', 71: 'si'
}

solresol_to_english = {
    'do': 'No, not, nor',
    're': 'And',
    'mi': 'My, mine',
    'fa': 'For, because',
    'sol': 'So',
    'la': 'In',
    'si': 'If'
}

# Function to translate MIDI note to Solresol syllable and then to English word
def translate_midi_to_english(midi_note):
    solresol_syllable = midi_to_solresol.get(midi_note, 'Unknown')
    english_word = solresol_to_english.get(solresol_syllable, 'Unknown')
    return solresol_syllable, english_word

# Function to handle MIDI input
def midi_input_handler():
    with mido.open_input() as port:
        print("Listening to MIDI input... Press keys on your MIDI keyboard.")
        for msg in port:
            if msg.type == 'note_on':
                midi_note = msg.note
                solresol_syllable, english_word = translate_midi_to_english(midi_note)
                print(f"MIDI Note: {midi_note}, Solresol: {solresol_syllable}, English Word: {english_word}")

# Main function to run the MIDI input handler
if __name__ == "__main__":
    try:
        midi_input_handler()
    except KeyboardInterrupt:
        print("\nTranslation stopped.")
