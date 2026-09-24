import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
n=0
def dec2bin(value):
    return [int(e) for e in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while (True):
    if GPIO.input(up):
        n+=1
        print(n,dec2bin(n))
        time.sleep(sleep_time)
        GPIO.output(leds,dec2bin(n))
    if GPIO.input(down)>0:
        if n > 0:
            n = n - 1
        print(n, dec2bin(n))
        GPIO.output(leds,dec2bin(n))
        time.sleep(sleep_time)