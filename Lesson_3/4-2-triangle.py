import RPi.GPIO as GPIO
import time

def binary(n):
    num = []
    while n > 1:
        num.append(n % 2)
        n = n // 2
    num.append(n)
    num += [0] * (8 - len(num))
    return num[::-1]

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

while True:
    try:
        print('Введите период:')
        period = int(input())
        if period > 0:
            n = 0
            while True:
                while n < 255:
                    print(n)
                    GPIO.output(dac, binary(n))
                    n += 1
                    time.sleep(period/512)
                while n > 0:
                    print(n)
                    GPIO.output(dac, binary(n))
                    n -= 1
                    time.sleep(period/512)
        else:
            print('Введите положительное число')
    except ValueError:
        print('Введите целое число')
    finally:
        GPIO.cleanup()