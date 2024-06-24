from machine import Pin, I2C, UART
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS
import framebuf
##https://diyprojectslab.com/raspberry-pi-pico-gps-tracker-using-neo-6m-oled-display/
reset = machine.Pin(10, machine.Pin.OUT)
reset.value(1)

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
device_list=i2c.scan()
print(len(device_list))

for i in range(0, len(device_list)):
    print(str(device_list[i]))
    
oled = SSD1306_I2C(128, 64, i2c)


#######
# Initialize GPS module
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
time_zone = -4
gps = MicropyGPS(time_zone)

def convert_coordinates(sections):
    if sections[0] == 0:  # sections[0] contains the degrees
        return None

    # sections[1] contains the minutes
    data = sections[0] + (sections[1] / 60.0)

    # sections[2] contains 'E', 'W', 'N', 'S'
    if sections[2] == 'S':
        data = -data
    if sections[2] == 'W':
        data = -data

    data = '{0:.6f}'.format(data)  # 6 decimal places
    return str(data)
#######


while True:
    length = gps_module.any()
    if length > 0:
        data = gps_module.read(length)
        for byte in data:
            message = gps.update(chr(byte))

    latitude = convert_coordinates(gps.latitude)
    longitude = convert_coordinates(gps.longitude)

    if latitude is None or longitude is None:
        oled.fill(0)
        oled.text("Data unavailable", 0, 25)
        oled.text("No coordinates", 0, 40)
        oled.show()
        continue

    
    oled.fill(0)
    oled.text('Satellites: ' + str(gps.satellites_in_use), 0, 0)
    oled.text('Lat: ' + latitude, 0, 12)
    print('Lat: ' + latitude)
    oled.text('Lon: ' + longitude, 0, 24)
    print('Lon: ' + longitude)
    print("date: ",  gps.date[0] , gps.date[1] , gps.date[2])
    oled.text('Date: ' + str(gps.date[1]) + '/' + str(gps.date[0]) + '/' + str(gps.date[2]), 0, 36)
    print("time: ",  gps.timestamp[0] , gps.timestamp[1] , gps.timestamp[2])
    oled.text('time: ' + str(gps.timestamp[0]) + ':' + str(gps.timestamp[1]) + ':' + str(gps.timestamp[2]), 0, 48)

    oled.show()