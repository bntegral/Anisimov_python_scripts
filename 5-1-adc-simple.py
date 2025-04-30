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

def adc():
    for v in range(256):
        GPIO.output(dac, binary(int(v)))
        time.sleep(0.001)
        #print (3.3 * v / 255, binary(int(v)))
        if GPIO.input(comp) == 1:
            print(v, 'Предполагаемое напряжение:', 3.3 * v / 255)
            break

dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        adc() 
finally:
    GPIO.cleanup()