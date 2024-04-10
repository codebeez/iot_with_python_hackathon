# Implement here
from machine import PWM
from utime import sleep

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": " ",
}

BASE_DELAY = 0.2
MORSE_DELAY_DICT = {".": 1, "-": 3, "intra": 1, " ": 3, "end": 7}

buzzer = PWM(15)
buzzer.freq(131)

morse_word = "SOS"
morse_code = " ".join([MORSE_CODE_DICT[char] for char in morse_word])


while True:
    try:
        for char in morse_code:
            if char in [".", "-"]:
                buzzer.duty_u16(1000)
                sleep(BASE_DELAY * MORSE_DELAY_DICT[char])
                buzzer.duty_u16(0)
                sleep(BASE_DELAY * MORSE_DELAY_DICT["intra"])
            else:
                buzzer.duty_u16(0)
                sleep(BASE_DELAY * (MORSE_DELAY_DICT[char] - MORSE_DELAY_DICT["intra"]))
        sleep(BASE_DELAY * (MORSE_DELAY_DICT["end"] - MORSE_DELAY_DICT["intra"]))
    except KeyboardInterrupt:
        break
buzzer.duty_u16(0)
