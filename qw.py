import mido
import tkinter as tk

# Function to convert MIDI note to RGB
def note_to_rgb(note):
    r = (note * 3) % 256
    g = (note * 5) % 256
    b = (note * 7) % 256
    return f'#{r:02x}{g:02x}{b:02x}'

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

def update_color(msg):
    if msg.type == 'note_on':
        color = note_to_rgb(msg.note)
        canvas.configure(bg=color)

# Continuously check for MIDI messages
def poll_midi():
    for msg in inport.iter_pending():
        update_color(msg)
    root.after(10, poll_midi)

root.after(10, poll_midi)
root.mainloop()

