import RPi.GPIO as GPIO
import time

def binary(n):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]


def adc():
    code = []
    GPIO.output(dac, [1] + [0] * 7)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append(0)
    GPIO.output(dac, [0] + [1] + [0] * 6)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append(0)
    GPIO.output(dac, [0] * 2 + [1] + [0] * 5)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append(0)
    GPIO.output(dac, [0] * 3 + [1] + [0] * 4)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append(0)
    GPIO.output(dac, [0] * 4 + [1] + [0] * 3)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append(0)
    GPIO.output(dac, [0] * 5 + [1] + [0] * 2)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append(1)
    else:
        code.append( 0)
    GPIO.output(dac, [0] * 6 + [1] + [0] * 1)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append( 1)
    else:
        code.append( 0)
    GPIO.output(dac, [0] * 7 + [1])
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        code.append( 1)
    else:
        code.append( 0)
    return code

dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        timestart = time.time()
        a = adc()
        print(time.time() - timestart)
        v = int(''.join([str(e) for e in a]), 2)
        print(v, 'Предполагаемое напряжение:', 3.3 * v / 255)
finally:
    GPIO.cleanup()
    