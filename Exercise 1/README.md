# Blink - The hello world of hardware

Welcome to the first exercise of the IoT with Python hackathon! The "Blink" exercise is often referred to as the "Hello World" of the hardware realm.

## Objective

Your task is to write a Python script that will make an LED blink on and off at regular intervals. This simple task helps you understand how to interact with hardware components using Python code.

## Instructions

1. Setup Your Hardware: In this case this is very easy, since the PI Pico has a built in led.

2. Write Your Code: Open VSCode and ensure the MicroPico plugin is active. Create a new Python file named blink.py. This file will contain your code to turn the LED on and off.

3. Code Structure:

- Import the necessary libraries from MicroPython to interact with the GPIO pins.
- Set the correct pin as an output.
- Use a loop to turn the LED on, wait for a second, turn it off, and wait again.

Example snippet:

```python
from machine import Pin
from utime import sleep


pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1)  # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")

```

1. Run Your Code: With your blink.py file open in VSCode, click the ▷ Run button. Your Raspberry Pi Pico should execute the script, and you should see the LED start to blink.

2. Debugging: If the LED does not blink, ensure you have the correct GPIO pin number in your code, and make sure your Raspberry Pi Pico is powered.

3. Going Further: Once you have the basic blinking LED, experiment with different on/off intervals.
