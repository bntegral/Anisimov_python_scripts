import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

def binary(n):
    return [int (elem) for elem in bin(n)[2:].zfill(8)]

def adc():
    j=128
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=64
    else:
        j+=64
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=32
    else:
        j+=32
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=16
    else:
        j+=16
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=8
    else:
        j+=8
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=4
    else:
        j+=4
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=2
    else:
        j+=2
    GPIO.output(dac, binary(j))
    time.sleep(0.005)
    if GPIO.input(comp)==0:
        j-=1
    else:
        j+=1
    if GPIO.input(comp)==0:
        j-=1
    return j

led=[21, 20, 16, 12, 7, 8, 25, 24]
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)
list_up = []
list_down = []

try:
    a = 0
    GPIO.output(troyka, 0)
    timestart = time.time()
    while a < 120:
        a = adc()
        v = 3.3 * a / 255
        print(a, 'Заряжаем, предполагаемое напряжение:', v)
        list_up.append(v)
        GPIO.output(led, binary(a))
    GPIO.output(troyka, 1)
    print('Разряжаем')
    while a > 36:
        a = adc()
        v = 3.3 * a / 255
        print(a, 'Разряжаем, предполагаемое напряжение:', v)
        list_up.append(a)
        GPIO.output(led, binary(a))
    
finally:
    timefinish = time.time() - timestart
    with open('/home/b04-406/Desktop/Scripts/data.txt', 'w') as f:
        f.writelines([str(e) + '\n' for e in list_up + list_down])
    with open('/home/b04-406/Desktop/Scripts/settings.txt', 'w') as f:
        f.write(str(len(list_up + list_down)/timefinish) + '\n' + str(3.3 / 255))
    print(timefinish, 0.005, timefinish/len(list_up + list_down), 3.3 / 255)
    print('Общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации проведённых измерений {}, шаг квантования АЦП {}'.format(timefinish, timefinish/len(list_up + list_down), len(list_up + list_down)/timefinish, 3.3 / 255))
    x = [timefinish/len(list_up + list_down) * i for i in range(len(list_up + list_down))]
    y = list_up + list_down
    pyplot.xlabel('t, c')
    pyplot.ylabel('U, В')
    pyplot.plot(x, y)
    pyplot.show()
    GPIO.cleanup()

