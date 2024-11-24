import RPi.GPIO as GPIO
import time
import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *

GPIO.setmode(GPIO.BOARD)  #   Broadcom Chip Numbering
GPIO.setup(LED_PIN_BOARD, GPIO.OUT)

#   Toggling LED output to test the output
try:
    while True:
        GPIO.output(LED_PIN_BOARD, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)
        GPIO.output(LED_PIN_BOARD,GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting test program...")
    GPIO.cleanup