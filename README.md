# audiobutton
Use a single GPIO button to cycle through generated audio

Uses [gpiozero](http://pythonhosted.org/gpiozero/) and [SoX](http://sox.sourceforge.net/)

```
sudo apt-get -y install python-gpiozero sox libsox-fmt-all
```
Defaults to GPIO 16 for input. Edit that inside of `audiobutton.py`
Also change the path to `tones.sh` in `audiobutton.py`

An external shell script is used to enable backgrounding the play utility, otherwise it won't be able to play the next item.

# Tones
1. Guitar strum
2. 30Hz - 120 Hz sweep
3. 100Hz - 2KHz sweep
4. 30 Hz - 20KHz sweep
5. 60 Hz tone
6. 100 Hz tone
7. 500 Hz tone
8. 1KHz tone
9. whitenoise
10. pinknoise
