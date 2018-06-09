import RPi.GPIO as GPIO
from time import sleep
import subprocess

PIN = 24        

def my_callback(channel):
    if channel == PIN:
        args = ['sudo', 'poweroff']
        # subprocess.Popen(args)
        print("power-off")

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback, bouncetime=200)

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
