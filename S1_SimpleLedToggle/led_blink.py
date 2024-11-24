import RPi.GPIO as GPIO
import time

#   GPIO 4 will be used as LED project GPIO
LED_PIN = 4
PHY_PIN = 16

GPIO.setmode(GPIO.BOARD)  #   Broadcom Chip Numbering
GPIO.setup(PHY_PIN, GPIO.OUT)

#   Toggling LED output to test the output
try:
    while True:
        GPIO.output(PHY_PIN, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)
        GPIO.output(PHY_PIN,GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting test program...")
    GPIO.cleanup