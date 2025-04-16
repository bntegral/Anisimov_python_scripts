import RPi.GPIO as GPIO

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

try:
    n = ''
    while n != 'q':
        n = input()
        try:
            float(n)
            try:
                n = int(n)
                if n < 0:
                    print('Введено отрицательное число')
                elif int(n) > 255:
                    print('Введено значение, превышающее возможности ЦАП')
                else:
                    print('Предполагаемое напряжение:', 3.3 * n / 256)
                    GPIO.output(dac, binary(int(n)))
            except ValueError:
                print('Введено не целое число')
        except ValueError:
            print('Введено не число')
finally:
    GPIO.cleanup()