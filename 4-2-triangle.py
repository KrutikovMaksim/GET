import RPi.GPIO as gpio
import time
import sys

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def decimal2binari(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

try:
    while(True):
        
        T = input("Введите период треугольного сигнала")

        if (T == "q"):
            break

        if (not T.isdigit()):
            print("Ошибка!! Данная строчка не является десятичным числом")
            continue


        t = int(T) / 256 / 2
        for i in range(256):
            gpio.output(dac, decimal2binari(i))
            time.sleep(t)
        for i in range(255, -1, -1):
            gpio.output(dac, decimal2binari(i))
            time.sleep(t)
        

finally:
    gpio.output(dac, 0)
    gpio.cleanup()