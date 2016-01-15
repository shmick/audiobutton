#!/usr/bin/env python
from gpiozero import Button, Buzzer
from signal import pause
from time import sleep
import os

button1 = None
while not button1:
    try:
        button1 = Button(16)
    except RuntimeError:
        pass

num = -1
prnt = 0
last = False

input_value = False

def released():
    input_value = True

def printer():
    print("playing song %s" % num)
    os.system("pkill play")
    sleep(.2)
    os.system("/home/pi/tones.sh %s" % num)

while True:
    sleep(.01)

    input_value = button1.is_pressed

    if (input_value == True) and (last == False):
        last = True
        prnt = 1
        num += 1
        sleep(.01)
        continue

    if (input_value == False) and (last == True):
        last = False
        sleep(.01)
        continue

    if (input_value == True) and (last == True):
        if (prnt == 1):
            if (num >= 11):
                num = 0
            if (num <= 9):
                printer()
            if (num >= 10):
                os.system("pkill play")
            prnt = 0
            sleep(.01)
        continue

pause()
