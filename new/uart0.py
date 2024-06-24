from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart.write('hello1234567890')
time.sleep(0.1)
readstr=uart.read(15) # read up to 5 bytes
print(readstr)