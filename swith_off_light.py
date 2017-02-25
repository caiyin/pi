import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

light = False


while True:
    i = GPIO.input(24)
    if i:
        print('down')
        while 1:
            i = GPIO.input(24)
            if not i:
                print('up')
                GPIO.output(25,light)
                light = not light
                break
    time.sleep(0.1)
