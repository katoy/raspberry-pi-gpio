# See
#  https://github.com/szazo/DHT11_Python

import RPi.GPIO as GPIO
import dht11
import time
import datetime

INTERVAL = 2

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print(result.temperature)
            print("Last valid input: %s" % str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)

        time.sleep(INTERVAL)

except KeyboardInterrupt:
    pass

GPIO.cleanup()    
