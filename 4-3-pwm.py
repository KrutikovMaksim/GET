import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

aux = 23

gpio.setup(aux, gpio.OUT)

pwm = gpio.PWM(aux, 1000)
pwm.start(0)
try:
    while(True):
        cofe = int(input("Введите число: "))
        pwm.start(cofe)

finally:
    pwm.stop()
    gpio.output(aux, 0)
    gpio.cleanup()