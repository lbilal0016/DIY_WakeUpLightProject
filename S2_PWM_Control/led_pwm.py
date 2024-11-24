import RPi.GPIO as GPIO
import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *

class LEDPWM:
    def __init__(self,pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        #   Set PWM frequency
        self.pwm = GPIO.PWM(self.pin, PWM_FREQUENCY)  
        #   Initial brightness
        self.pwm.start(0)

    def set_brightness(self, brightness):
            if 0 <= brightness <= 100:
                self.pwm.ChangeDutyCycle(brightness)
            else:
                print("Please enter a pwm duty cycle between 0 - 100")
            
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

    def __enter__(self):
         return self
    
    def __exit__(self, exc_type, exc_value, traceback)
         self.cleanup()




