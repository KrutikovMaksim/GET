import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def decimal2binari(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def print_volt(num):
    print("Напряжение на выходе V = {:.3f} в".format(num / 256.0* 3.3))

try:
    while(True):       
        str = input("Введите деятичное число от 0 до 255:")

        if (str == "q"):
            break

        try:
            num = int(str)
        except ValueError:
            print("Ошибка!! Данная строчка не является десятичным числом")
        else:
            if (num < 0):
                print("Введенное число не должно быть отрицательным")
                continue

            if (num > 255):
                print("Введенное число не должно быть больше 256")
                continue    

            gpio.output(dac, decimal2binari(num))

            print_volt(num)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()