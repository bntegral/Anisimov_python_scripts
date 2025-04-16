import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

p = GPIO.PWM(27, 1000)
p.start(0)

try:
    while True:
        z = float(input())
        print(3.3 * z / 100)
        p.ChangeDutyCycle(z)
            
finally:
    GPIO.cleanup()
    