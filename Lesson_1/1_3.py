import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

try:
    input_value = GPIO.input(17)

    GPIO.output(18, input_value)
    time.sleep(3)

finally:
    GPIO.cleanup()