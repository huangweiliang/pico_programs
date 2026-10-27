from machine import Pin
import time

button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("Button pressed")
    else:
        print("Button released")

    time.sleep(0.1)