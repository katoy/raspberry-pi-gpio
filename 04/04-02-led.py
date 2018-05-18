import RPi.GPIO as GPIO
from time import sleep

PIN = 25
INTERVAL_SEC = 0.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN, not GPIO.input(PIN))
        sleep(INTERVAL_SEC)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
