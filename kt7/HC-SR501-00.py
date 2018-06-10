# coding: UTF-8
# See 
# https://umiushizn.blogspot.com/2017/10/hc-sr501raspberry-pi.html

# case in Python 2.6~
from __future__ import print_function

import sys
import time
import RPi.GPIO as GPIO

SLEEP_TIME = 1
SENSOR_GPIO = 18 # 18 # 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_GPIO, GPIO.IN)

try:
  while True:
    if GPIO.input(SENSOR_GPIO):
      message = "\r 動いた    \r"
    else:
      message = "\r 動いてない\r"

    # python2
    print(message, end="")
    sys.stdout.flush()
    # python3 
    # print(message, flush=True,end="")

    time.sleep(SLEEP_TIME)

except KeyboardInterrupt:
      pass

GPIO.cleanup()
print("end")
