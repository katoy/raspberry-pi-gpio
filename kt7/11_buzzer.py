# See
#  http://osoyoo.com/ja/2017/06/28/raspberry-pi-3-buzzer/
#  http://www6.plala.or.jp/empty_space/note0122.html

import RPi.GPIO as GPIO
import time

BuzzerPin = 25    # GPIO 25

SCALE_Hz = [262, 294, 330, 349, 392, 440, 494, 523]
Pi_Hz = 850    # 960 For home use 850
Po_Hz = 680    # 770 For home use 680

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BuzzerPin, GPIO.OUT)
        GPIO.output(BuzzerPin, GPIO.LOW)

def loop():
        while True:
                p = GPIO.PWM(BuzzerPin, 1)
                p.start(50)
                for Hz in SCALE_Hz:
                        p.ChangeFrequency(Hz)
                        time.sleep(0.3)
                p.stop()
                time.sleep(1)

                p.start(50)
                for i in range(0, 4) :
                        p.ChangeFrequency(Pi_Hz)
                        time.sleep(0.65)
                        p.ChangeFrequency(Po_Hz)
                        time.sleep(0.65)
                p.stop()
                time.sleep(2)
def destroy():
        GPIO.output(BuzzerPin, GPIO.LOW)
        GPIO.cleanup() # Release resource

if __name__ == '__main__': # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
                destroy()

