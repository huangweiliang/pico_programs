import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
gled_onboard = machine.Pin(1, machine.Pin.OUT)
yled_onboard = machine.Pin(5, machine.Pin.OUT)
rled_onboard = machine.Pin(17, machine.Pin.OUT)
while True:
    led_onboard.value(1)
    gled_onboard(1)
    utime.sleep(0.2)
    yled_onboard(1)
    utime.sleep(0.2)

    rled_onboard(1)
    utime.sleep(0.2)
    
    led_onboard.value(0)
    gled_onboard(0)
    yled_onboard(0)
    rled_onboard(0)
    utime.sleep(0.2)