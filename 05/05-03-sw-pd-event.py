import RPi.GPIO as GPIO
from time import sleep

pin = 25
sw = 24
interval_sec = 0.05

def my_callback(channel):
    if channel != sw:
        return

    global stat
    stat = not stat
    GPIO.output(pin, stat)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(sw, GPIO.RISING, callback=my_callback, bouncetime=200)

stat = False
try:
    while True:
        sleep(interval_sec)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
