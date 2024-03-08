from machine import Pin
from time import sleep_ms

sound = Pin(0, Pin.IN)

if __name__ == "__main__":
    while True:
        print(sound.value())
        if sound.value() == 1:
            print("No sound")
        else:
            print("Sound detected!")
        sleep_ms(500)
