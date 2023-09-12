# Setup
```
python -m venv myenv
source myenv/bin/activate
pip install mido python-rtmidi
```
For Windows:

```
python -m venv myenv
myenv\Scripts\activate
pip install mido python-rtmidi --prefer-binary
```

# MIDI to Solresol Translator

This Python script translates MIDI notes to Solresol syllables and then to English words. It uses dictionaries to map MIDI notes to Solresol syllables and Solresol syllables to English words. The script listens to a MIDI input device (e.g., Arturia MiniLab mkII) and displays translations in real-time.

## Features

- Translates MIDI notes to Solresol syllables.
- Translates Solresol syllables to English words.
- Real-time translation and display of MIDI input.

## Requirements

- Python 3.x
- Mido library (for MIDI input)
- Arturia MiniLab mkII or a MIDI input device


```
Listening to Arturia MiniLab mkII... Press keys on your MIDI keyboard.
MIDI Note: 60, Solresol: do
Solresol: do, English Word: No, not, nor
MIDI Note: 62, Solresol: re
Solresol: re, English Word: And
```
