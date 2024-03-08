# Displaying data

In this fourth exercise of the IoT with Python hackathon, you will delve into the world of data visualization using small displays connected to your Raspberry Pi Pico. You'll work with two common types of display modules: an LCD and an OLED.

## Preparation

Ensure to copy the file in the `external_libraries` folder to the `lib` folder on the Pi. See the general README for instructions

## Part 1: LCD - Interfacing and Basic Display

### Objective

Learn to interface an LCD with your Raspberry Pi Pico and display text messages.

### Resources

https://electrocredible.com/raspberry-pi-pico-lcd-16x2-i2c-pcf8574-micropython/

### Instructions

1. Setup Your Hardware: Connect an LCD display to your Raspberry Pi Pico. If you're using an I2C adapter (like the PCF8574), it will simplify your wiring and code.

2. Write Your Code: Create a new Python file lcd_display.py. Use the I2C library in MicroPython to establish communication with the LCD and send text to be displayed.

3. Display Static Text: First, try displaying a simple static message, like "Hello, Hackathon!"

4. Display Dynamic Data: Next, extend your script to display dynamic information. This could be sensor data you've collected, timestamps, or even a counter.

5. Test and Debug: Ensure that your LCD displays the text correctly. Troubleshoot any issues related to display clarity, text formatting, or I2C communication.

## Part 2: OLED - Advanced Graphics and Text

### Objective

Use an OLED display to show both text and simple graphics, providing a richer interface for your projects.

### Resources

https://randomnerdtutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/

### Instructions

1. Setup Your Hardware: Connect an SSD1306 OLED display to your Raspberry Pi Pico. This will typically use an I2C connection as well.

2. Write Your Code: Create a Python file oled_display.py. Utilize the ssd1306 library available in MicroPython to control the OLED.

3. Implement Text Display: Start by showing basic text on the OLED. You might display system information, sensor readings, or any other text-based data.

4. Incorporate Graphics: Go beyond text by including simple graphics or animations. This could be anything from progress bars and icons to basic shapes representing data trends or statuses.

5. Integrate with Sensors: Optionally, if you've completed previous exercises, integrate sensor data into your display output. For example, show temperature readings graphically or represent sound levels visually.

6. Test and Debug: Validate that both text and graphics render correctly on the OLED. Address any visual glitches or data update issues you encounter.
