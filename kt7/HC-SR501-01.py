#-*- coding: utf-8 -*-

# See
# https://qiita.com/cigalecigales/items/4cf9c16f24d1de92ec7d
# http://henrysbench.capnfatz.com/henrys-bench/arduino-sensors-and-input/arduino-hc-sr501-motion-sensor-tutorial/

import time
import RPi.GPIO as GPIO

INTAVAL = 5
SLEEPTIME = 1
SENSOR_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time() - INTAVAL

try:
  while True:
    # print(GPIO.input(SENSOR_PIN))
    if (GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
      st = time.time()
      print("人を感知しました " + time.strftime("%H:%M:%S", time.localtime()))

    time.sleep(SLEEPTIME)

except KeyboardInterrupt:
      pass

GPIO.cleanup()
print("end")
