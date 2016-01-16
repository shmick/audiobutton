#!/usr/bin/env python
from gpiozero import Button, LED
from signal import pause
from time import sleep
import os

green = LED(47)
green.off()

# A hack to get around a known bug
# https://github.com/RPi-Distro/python-gpiozero/issues/50
button1 = None
while not button1:
    try:
        button1 = Button(26, bounce_time=0.2)
    except RuntimeError:
        pass

num = 0
playloop = 0
last = False

def blinkled():
    green.off()
    if num != 99:
        green.blink(on_time=.2, off_time=.3, n=(num))
    elif num == 99:
        green.blink(on_time=.1, off_time=.1, n=30)

def audioplay():
    print("playing song %s" % num)
    os.system("pkill play")
    sleep(.2)
    os.system("/home/pi/tones.sh %s" % num)
    blinkled()

while True:
    sleep(.01)

    input_value = button1.is_pressed

    if   (input_value == True) and (last == False):
         last = True
         playloop = 1
         num += 1
         sleep(.01)
    elif (input_value == False) and (last == True):
         last = False
         sleep(.01)
    elif (input_value == True) and (last == True):
          if (playloop == 1):
            if (num == 1):
               button_press_timer = 0
               while True:
                   if (button1.is_pressed == True) : # while button is still pressed down
                      button_press_timer += 1 # keep counting until button is released
                      print("button hold count %s" % button_press_timer)
                      sleep(1)
                   else: # button is released, figure out for how long
                       if (button_press_timer > 4) : # pressed for > 4 seconds
                           num = 99
                           audioplay()
                           num = 0
                       elif (button_press_timer < 4) : # pressed for < 4 seconds
                           audioplay()
                       break
                       button_press_timer = 0
            elif (num >= 2) and (num <= 10):
                 audioplay()
            elif (num == 11):
                 print("Stopping on count %s" % num)
                 os.system("pkill play")
                 print("Press button again to start over")
                 num = 0

            playloop = 0
pause()
