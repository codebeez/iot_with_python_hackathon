# Web connectivity

In this final exercise of the IoT with Python hackathon, you'll explore the capabilities of the Raspberry Pi Pico to connect to the web and serve data over a network. This exercise aims to familiarize you with basic web server concepts, allowing your IoT devices to interact with web-based interfaces.

## Objective

Create a simple web server on your Raspberry Pi Pico that can control an LED and display a random value on a web page. You will write MicroPython code to manage web requests and serve dynamic content, turning the Raspberry Pi Pico into a basic IoT device accessible over a local network.

## Resources

https://randomnerdtutorials.com/raspberry-pi-pico-web-server-micropython/

## Instructions

1. Setup Your Hardware: Ensure your Raspberry Pi Pico is connected to your computer.

2. Network Configuration: Modify the provided `webserver_example,py` script to include your Wi-Fi credentials. Replace PLACEHOLDER with your network's SSID and password.

3. Understand the Web Server Code: Analyze the provided script to understand how the Raspberry Pi Pico establishes a Wi-Fi connection, listens for incoming HTTP requests, and serves web pages.

4. Implement Control Logic: The script includes routes to turn the LED on or off and to fetch a new random value. Understand how these routes are processed and how the server responds to different requests.

5. Serve Dynamic Content: Modify the webpage function to customize the HTML content. You might add additional controls, display sensor data, or provide links to other resources.

6. Run and Test Your Web Server:

- Run the script on your Raspberry Pi Pico and monitor the serial output to confirm it connects to your Wi-Fi network. You can use the MicroPico plugin for this
- Use a web browser on a device connected to the same network to access the web server using the Raspberry Pi Pico's IP address.
- Test the LED control and the fetch value functionality to ensure they work as expected.

7. Debugging:

- If you encounter issues with the Wi-Fi connection, verify your credentials and ensure your network allows new devices to connect.
- Check the console output for error messages or clues if the web server does not respond as expected.

8. Challenges:

- Enhance the web server functionality with additional routes or control options.
- Integrate sensor data into the web page, updating it in real-time or on request.
- Implement basic security measures, such as limiting access to certain functions or rate-limiting requests.
