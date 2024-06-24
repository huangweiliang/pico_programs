import machine
from time import sleep
import utime
from pico_i2c_lcd import I2cLcd
from machine import Pin, I2C


##https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico#xenforo-comments-3710356
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    print(I2C_ADDR)
    voltage = potentiometer.read_u16() * conversion_factor
    lcd.clear()
    lcd.blink_cursor_on()
    lcd.putstr("ADC:"+str(voltage)+"\n")
    print(voltage)
    ##lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
    ##lcd.putstr("Tom's Hardware")
    sleep(1)