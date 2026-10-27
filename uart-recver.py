from machine import UART, Pin
import time

uart = UART(
    1,
    baudrate=115200,
    tx=Pin(4),
    rx=Pin(5),
    bits=8,
    parity=None,
    stop=1
)

print("UART receiver started...")

while True:
    if uart.any():
        data = uart.read()
        if data:
            #print("RX HEX:", data.hex(' '))
            print("i am receiver - RX RAW:", data)

    time.sleep_ms(10)