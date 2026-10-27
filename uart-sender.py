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

counter = 0

while True:
    message = "i am sender --- Hello UART! Counter: {}\r\n".format(counter)

    uart.write(message)
    print("Sent:", message.strip())

    counter += 1
    time.sleep(1)