from machine import Pin, I2C
from sh1106 import SH1106_I2C

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
oled = SH1106_I2C(128, 64, i2c, None, addr=0x3C)
oled.sleep(False)
oled.text("Test", 0, 0)
oled.show()
