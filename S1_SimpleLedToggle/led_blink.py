import RPi.GPIO as GPIO
import time

#   GPIO 4 will be used as LED project GPIO
LED_PIN = 4

GPIO.setmode(GPIO.BCM)  #   Broadcom Chip Numbering
GPIO.setup(LED_PIN, GPIO.OUT)

#   Toggling LED output to test the output
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting test program...")
    GPIO.cleanup