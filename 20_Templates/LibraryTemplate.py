import RPi.GPIO as GPIO
import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *

class TemplateClass:
    def __init__(self,pin):
        #   Class constructor
            
    def cleanup(self):
        #   cleanup function
        GPIO.cleanup()

    def __enter__(self):
         return self
    
    def __exit__(self, exc_type, exc_value, traceback):
         self.cleanup()




