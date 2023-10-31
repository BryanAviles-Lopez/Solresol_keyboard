import mido
import matplotlib.pyplot as plt

# Set up the MIDI input
midi_inputs = mido.get_input_names()
if 'Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0' in midi_inputs:
    inport = mido.open_input('Arturia MiniLab mkII:Arturia MiniLab mkII MIDI 1 24:0')
else:
    print("Arturia MiniLab mkII not found. Using default MIDI input.")
    inport = mido.open_input()

# Function to visualize the note in matplotlib
def visualize_note(note, velocity):
    plt.figure(figsize=(10, 6))
    
    # Display the note and its velocity
    plt.bar(["Note", "Velocity"], [note, velocity])
    
    # Set the limits for better visualization
    plt.ylim(0, 130)
    plt.title(f"Note: {note} | Velocity: {velocity}")
    plt.show(block=False)
    plt.pause(1)
    plt.close()

print("Press keys on your Arturia MiniLab keyboard...")

# Continuously check for MIDI messages
for msg in inport:
    if msg.type == 'note_on':
        visualize_note(msg.note, msg.velocity)

