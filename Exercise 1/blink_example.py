from machine import Pin
from utime import sleep

pin = Pin(15, Pin.OUT)
pin2 = Pin("LED", Pin.OUT)

pin2.toggle()

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        pin2.toggle()
        sleep(1)  # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
