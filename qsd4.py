import mido
import tkinter as tk
import pandas as pd

# Define MIDI notes for black keys (acting as spacebar or end of input)
BLACK_KEYS = [49, 51, 54, 56, 58, 61, 63]

# Define a color mapping for Solresol syllables
solresol_color_mapping = {
    'Do': 'red',
    'Re': 'orange',
    'Mi': 'yellow',
    'Fa': 'lightgreen',
    'Sol': 'green',
    'La': 'teal',
    'Si': 'lightblue'
}

# Mapping between MIDI notes and Solresol notes for natural keys on the keyboard
MIDI_TO_SOLRESOL = {
    48: 'Do',
    50: 'Re',
    52: 'Mi',
    53: 'Fa',
    55: 'Sol',
    57: 'La',
    59: 'Si',
    60: 'Do',
    62: 'Re',
    64: 'Mi',
    65: 'Fa',
    67: 'Sol',
    69: 'La',
    71: 'Si'
}

# Load the Excel file into a DataFrame
try:
    df_solresol = pd.read_excel("/home/mpcr/Downloads/Copy of Pandas Solresol Dictionary.xlsx")
    print("Excel file loaded successfully.")
except Exception as e:
    print("Error loading Excel file:", e)
    exit()

# Create a dictionary from the DataFrame
solresol_dict = pd.Series(df_solresol['No, not, nor'].values, index=df_solresol['Do']).to_dict()

# Set up the tkinter window
root = tk.Tk()
root.title("MIDI to Solresol Translator")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

label = tk.Label(root, text="", font=('Helvetica', 24), bg='white', width=20, height=2)
label.place(relx=0.5, rely=0.5, anchor='center')

# Define a variable to accumulate Solresol syllables into a word
solresol_word = ''

def update_translation(msg):
    global solresol_word  # To modify the global variable
    
    if msg.type == 'note_on':
        # If a black key is pressed, reset the accumulated word
        if msg.note in BLACK_KEYS:
            if solresol_word:
                # Process the accumulated Solresol word
                meaning = solresol_dict.get(solresol_word, 'Translation not found')
                color = solresol_color_mapping.get(solresol_word[:2], 'white')
                label.config(text=meaning, bg=color)
                print(f"Processed word: {solresol_word}, Meaning: {meaning}, Color: {color}")
            solresol_word = ''  # Reset the word
        elif msg.note in MIDI_TO_SOLRESOL:
            # Accumulate the syllable
            solresol_note = MIDI_TO_SOLRESOL[msg.note]
            solresol_word += solresol_note
            print(f"Accumulated Solresol word: {solresol_word}")

# Set up the MIDI input
midi_inputs = mido.get_input_names()
print("Available MIDI Inputs:", midi_inputs)

# Attempt to connect to the MIDI device
try:
    inport = mido.open_input('Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0')
    print("Connected to Arturia MiniLab mkII")
except Exception as e:
    print("Could not find Arturia MiniLab mkII. Please ensure it is connected and the correct name is used.")
    exit()

# Continuously check for MIDI messages
def poll_midi():
    for msg in inport.iter_pending():
        update_translation(msg)
    root.after(10, poll_midi)

root.after(10, poll_midi)
root.mainloop()

