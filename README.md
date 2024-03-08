# iot_with_python_hackathon

A hackathon around using Python on a Raspberry PI for IoT purposes such as reading sensors, running a server and writing data to screens.

## Prerequisit

In order to have Raspberry PI Pico run Python code, the MicroPython firmware has been flashed to the RP2040 chip. This allows us to write Python code on our machine, and simply drag & drop the file and have the Pico run the code automatically. If you are interested in the flashing processes, you can read more about it [here](https://micropython.org/download/RPI_PICO/).

To make the development process easy, the VSCode plugin [MicroPico](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go) is used in this Hackathon. Make sure you have it installed.

## Resources

### Adding external libraries to the PI Pico

While the MicroPython firmware comes with a set of libraries, some senors, screens and other devices require external libraries. Normally you would just `pip install` or `poetry add` but this does not work for the Pico. Instead you need to drag&drop a `.py` file from you machine into the filesystem of the PI Pico. Luckily the `MicroPico` extension (that you should have installed, see above) makes this very easy. Simply open the VSCode command pallet (`cmd+shift+p` on Mac) and type `Toggle Virtual File System` and select the command that comes up. This will mount the file system of the PI Pico directly in VSCode and allows you to drop your files directly in the correct directory.

After mounting the file system, there should be a folder in the root called `lib`. If the folder isn't there, simply create it and make sure you name it `lib`. This is where MicroPython will look for external libraries. Any file in here can be imported as `from file_name import class_name`.

Some general examples [here](https://peppe8o.com/adding-external-modules-to-micropython-with-raspberry-pi-pico/).

### Running code on the PI Pico

Now that you know how to mount the file system, we can talk about how to run the code you write on the PI Pico. Conveniently the MicroPico plugin makes this very easy for us. When you have a `.py` file open, you should see a `▷ Run` button in the status bar at the bottom of the screen. Clicking this will automatically copy your code into the correct place, reset the Pi and run the code.

Important note: just running the file doesn’t copy it permanently to the board’s filesystem. This means that if you unplug it from your computer and apply power to the board, nothing will happen because it doesn’t have any Python files saved on its filesystem. The Run function is useful to test the code, but if you want to upload it permanently to your board, you need to create and save a file to the board filesystem. MicroPython will automatically run a file called `main.py` on boot.

## Exercies

During this Hackathon the following exercises are prepared. Of course you are free to combine the skills you learn and build something useful for yourself.

- Exercise 1 - Blink
- Exercise 2 - Morse
- Exercise 3 - Sensors (dht11)
- Exercise 4 - Oled + sensor
- Exercise 5 - IoT

Good luck and have fun!
