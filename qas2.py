import mido
import tkinter as tk
import pandas as pd

# Load the Excel file into a DataFrame
df_solresol = pd.read_excel("/home/mpcr/Downloads/Copy of Pandas Solresol Dictionary.xlsx")

# Mapping between MIDI notes and Solresol notes for natural keys on the keyboard
MIDI_TO_SOLRESOL = {
    60: 'Do',
    62: 'Re',
    64: 'Mi',
    65: 'Fa',
    67: 'Sol',
    69: 'La',
    71: 'Si'
}

# Set up the MIDI input
midi_inputs = mido.get_input_names()
if 'Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0' in midi_inputs:
    inport = mido.open_input('Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0')
else:
    print("Arturia MiniLab mkII not found. Using default MIDI input.")
    inport = mido.open_input()

# Create a dictionary from the DataFrame for quick lookup
solresol_dict = dict(zip(df_solresol['Solresol Notes'], df_solresol['Meanings']))

# Set up the tkinter window
root = tk.Tk()
root.title("MIDI to Solresol Translator")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

label = tk.Label(root, text="", font=('Helvetica', 24))
label.place(relx=0.5, rely=0.5, anchor='center')

def update_translation(msg):
    if msg.type == 'note_on' and msg.note in MIDI_TO_SOLRESOL:
        solresol_note = MIDI_TO_SOLRESOL[msg.note]
        meaning = solresol_dict.get(solresol_note, '')
        label.config(text=meaning)

# Continuously check for MIDI messages
def poll_midi():
    for msg in inport.iter_pending():
        update_translation(msg)
    root.after(10, poll_midi)

root.after(10, poll_midi)
root.mainloop()

