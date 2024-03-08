# Reading data from the real world

In this third exercise of the IoT with Python hackathon, you'll venture into the realm of sensor integration with the Raspberry Pi Pico. You'll work with three different sensors: DHT11/DHT22 for temperature and humidity readings, an RGB LED for visual feedback, and a sound sensor for audio input. By interfacing with these diverse sensors, you'll gain a well-rounded perspective on collecting and responding to various types of environmental data.

## Preparation

Ensure to copy the file in the `external_libraries` folder to the `lib` folder on the Pi. See the general README for instructions

## Part 1: DHT11/DHT22 - Air Quality Monitoring

### Objective

Use the DHT11 or DHT22 sensor to measure temperature and humidity, then print these values to the console. These readings can serve as basic indicators for monitoring air quality.

### Resources

Use this tutorial to connect the sensor to the correct pins: https://randomnerdtutorials.com/raspberry-pi-pico-dht11-dht22-micropython/

### Instructions

1. Setup Your Hardware: Connect the DHT11 or DHT22 sensor to your Raspberry Pi Pico according to the wiring instructions provided in the tutorial links.

2. Write Your Code: Create a new Python file air_quality.py. Utilize the dht library in MicroPython to interact with the sensor and retrieve temperature and humidity data.

3. Display the Data: Print out the temperature and humidity readings in a readable format. Consider adding timestamps to each reading to track changes over time.

4. Test and Debug: Ensure that your script reliably reads and displays the sensor data. Address any connectivity or data retrieval issues you encounter.

## Part 2: RGB LED - Visual Feedback

### Objective

Control an RGB LED to display different colors based on predefined conditions. For instance, you could change the LED's color based on temperature ranges captured by the DHT sensor.

### Resources

Use this tutorial to connect the sensor to the correct pins: https://how2electronics.com/controlling-rgb-led-using-raspberry-pi-pico/

### Instructions

1. Setup Your Hardware: Wire the RGB LED to your Raspberry Pi Pico. Each color pin of the LED should connect through a resistor to a separate GPIO pin.

2. Write Your Code: Create a new Python file rgb_control.py. Write functions to turn the RGB LED different colors.

3. Integrate with Temperature Data: Optionally, integrate this part with the DHT sensor readings from Part 1. For example, display blue for cool temperatures, green for moderate, and red for warm.

4. Test and Debug: Verify that the LED changes colors as expected and refine your conditions or color functions as needed.

## Part 3: Sound Sensor - Audio Trigger

### Objective

Use a sound sensor to detect noise and execute an action when a certain threshold is exceeded, such as lighting up the RGB LED or printing a message.

### Resources

Use this tutorial to connect the sensor to the correct pins: https://how2electronics.com/voice-activated-light-with-sound-sensor-raspberry-pi-pico/

### Instructions

1. Setup Your Hardware: Connect the sound sensor to your Raspberry Pi Pico, ensuring that you have the output going to one of the GPIO pins.

2. Write Your Code: Create a Python file sound_trigger.py. Write code to monitor the sound sensor's output and trigger an action when the detected sound exceeds a predetermined threshold.

3. Create a Response: Define a response for triggering the threshold. This could involve activating the RGB LED, outputting a sound, or displaying a message.

4. Test and Debug: Experiment with different noise levels to calibrate your threshold and ensure that the sensor responds as intended.
