import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)

gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)

gpio.setup(comp, gpio.IN)

def decimal2binari(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    for i in range(255):
        dac_new = decimal2binari(i)
        gpio.output(dac, dac_new)
        comp_value = gpio.input(comp)
        
        time.sleep(0.05)

        if comp_value == 0:
            return i

try:
    while True:
        value = adc()
        if value != 0:
            print("Цифровое значение равно = ", value)
            print("Напряжение на выходе V = {:.4f} В".format(value * 3.3 / 256))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()