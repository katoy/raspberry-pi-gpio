import RPi.GPIO as GPIO
from time import sleep

PIN = 25
INTERVAL_SEC = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

while True:
    GPIO.output(PIN, not GPIO.input(PIN))
    sleep(INTERVAL_SEC)
