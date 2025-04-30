import RPi.GPIO as GPIO
import time

def binary(n):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]
def adc():
    code = []
    while len(code) != 8:
        code_copy = code.copy()
        code_copy += [1] + [0] * (7 - len(code))
        GPIO.output(dac, code_copy)
        time.sleep(0.001)
        #print (3.3 * v / 255, binary(int(v)))
        if GPIO.input(comp) == 0:
            code += [1]
            break
        else:
            code += [0]
    return code + [1] * (8 - len(code))

dac = [6, 12, 5, 0, 1, 7, 11, 8][::-1]
comp = 14
troyka = 13
led = [9, 10, 22, 27, 17, 4, 3, 2][::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


try:
    while True:
        timestart = time.time()
        a = adc()
        print(time.time() - timestart)
        GPIO.output(led, a)
finally:
    GPIO.cleanup()