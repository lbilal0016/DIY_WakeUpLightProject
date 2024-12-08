import RPi.GPIO as GPIO
import pigpio
import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *

class LEDPWM:
    def __init__(self,pin):
        self.pin = pin
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(self.pin, PWM_FREQUENCY)
        self.pi.set_PWM_range(self.pin, 100)

    def set_brightness(self, brightness):
            if 0 <= brightness <= 100:
                self.pi.set_PWM_dutycycle(self.pin, brightness)
            else:
                print("Please enter a pwm duty cycle between 0 - 100")
    
    def calculateDutyCycleFromTimeRemaining(self, minutesRemaining):
        if not 0 <= minutesRemaining < 60:
            raise ValueError("Invalid arguments. Remaining minutes must be in range [0 - 59]")  
        
        #   PWM Duty Cycle calculation begins with minutes remaining smaller than time elapsed between dawn and sunrise
        if minutesRemaining > DAWN_TO_SUNRISE_MIN:
             dutyCycle = 0
        else:
            dutyCycle = 1 - (minutesRemaining / DAWN_TO_SUNRISE_MIN)
        return int(dutyCycle * 100)
            
    def cleanup(self):
        self.pi.set_PWM_dutycycle(self.pin, 0)
        self.pi.stop()

    def __enter__(self):
         return self
    
    def __exit__(self, exc_type, exc_value, traceback):
         self.cleanup()




