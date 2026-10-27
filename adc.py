from machine import ADC, Pin
import time

# GPIO28 = ADC2
adc = ADC(Pin(28))

while True:
    raw = adc.read_u16()

    # 转换成电压 (0 ~ 3.3V)
    voltage = raw * 3.3 / 65535

    print(f"ADC2 Raw: 0x{raw:04X}",  "Voltage: {:.3f} V".format(voltage))

    time.sleep(0.5)