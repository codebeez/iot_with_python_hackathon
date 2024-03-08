# Blinking on steriods - Communcation with light# Blink Exercise - Getting Started with Hardware Basics

Building on the foundation laid in the "Blink" exercise, this second challenge of the IoT with Python hackathon elevates your interaction with hardware through a more nuanced application: communicating using Morse code. This exercise blends the simplicity of blinking an LED with the complexity of encoding and transmitting information.

## Objective

Your task is to create a Python script that translates a given string into Morse code and then uses an LED to transmit that message. This exercise not only tests your understanding of GPIO pin manipulation but also introduces basic data encoding and transmission concepts.

## Instructions

1. Understand Morse Code: Morse code represents characters as sequences of dots (short blinks) and dashes (long blinks). For instance, the letter "E" is a single dot, and "T" is a single dash. You'll need to create a mapping in your Python script to translate each letter into its Morse code equivalent.

2. Prepare Your Script:

- Use the provided Python file named morse.py.
- Define a dictionary in your script to map each letter and number to its Morse code representation. Include a space mapping to handle pauses between words.

Example snippet:

```python
MORSE_CODE_DICT = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
'4': '....-', '5': '.....', '6': '-....', '7': '--...',
'8': '---..', '9': '----.', '0': '-----', ' ': ' '
}
```

1. Implement the Encoding and Blinking:

- Loop through the input string, look up each character in your Morse code dictionary, and convert the entire message into a sequence of dots and dashes.
- Use short blinks for dots, long blinks for dashes, and pauses to separate individual letters and words.

2. Run and Test Your Code:

- Input a message into your script and observe the LED blinking out the Morse code. Verify the accuracy of the transmission using an online reference, such as [this one](https://morsecode.world/international/translator.html).

3. Debugging:

- If the LED does not blink correctly, check your character mappings, ensure your timing intervals for dots, dashes, and spaces are distinct, and validate your loop logic for encoding and blinking.

4. Challenges:

- Enhance your script to accept dynamic input, allowing users to input their messages.
- Implement an option to adjust the transmission speed.
