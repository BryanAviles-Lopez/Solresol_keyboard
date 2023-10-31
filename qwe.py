import mido
import tkinter as tk

# Define note-to-color and note-to-text mappings
NOTE_TO_COLOR = {
    'C': 'red',
    'C#': 'orange',
    'D': 'yellow',
    'D#': 'light green',
    'E': 'green',
    'F': 'teal',
    'F#': 'light blue',
    'G': 'red',
    'G#': 'orange',
    'A': 'yellow',
    'A#': 'light green',
    'B': 'green'
}

NOTE_TO_TEXT = {
    'C': 'do',
    'C#': 're',
    'D': 'mi',
    'D#': 'fa',
    'E': 'sol',
    'F': 'la',
    'F#': 'si',
    'G': 'do',
    'G#': 're',
    'A': 'mi',
    'A#': 'fa',
    'B': 'sol'
}

# Function to get note name from MIDI note number
def get_note_name(midi_note):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[midi_note % 12]

# Set up the MIDI input
midi_inputs = mido.get_input_names()
if 'Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0' in midi_inputs:
    inport = mido.open_input('Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0')
else:
    print("Arturia MiniLab mkII not found. Using default MIDI input.")
    inport = mido.open_input()

# Set up the tkinter window
root = tk.Tk()
root.title("MIDI Color Viewer")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

label = tk.Label(root, text="", font=('Helvetica', 24))
label.place(relx=0.5, rely=0.5, anchor='center')

def update_color(msg):
    if msg.type == 'note_on':
        note_name = get_note_name(msg.note)
        color = NOTE_TO_COLOR.get(note_name, 'white')
        text = NOTE_TO_TEXT.get(note_name, '')
        canvas.configure(bg=color)
        label.config(text=text)

# Continuously check for MIDI messages
def poll_midi():
    for msg in inport.iter_pending():
        update_color(msg)
    root.after(10, poll_midi)

root.after(10, poll_midi)
root.mainloop()

