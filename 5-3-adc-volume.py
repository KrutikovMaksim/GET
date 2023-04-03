import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binari(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, decimal2binari(k))
        comp_value = gpio.input(comp)
        time.sleep(0.05)

        if comp_value ==0:
            k -= 2**i
    return k

try:
    while True:
        i = adc()
        gpio.output(leds, decimal2binari(i))
        if i != 0:
            print(i, "{:2f} v".format(3.3*i/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()