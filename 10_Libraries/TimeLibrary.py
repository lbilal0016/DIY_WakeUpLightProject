import RPi.GPIO as GPIO
import sys
from datetime import datetime, timedelta
import time
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

class wakeUpTimeHourAndMinute():
    def __init__(self, wakeUpHour=None, wakeUpMinute=None):
        if wakeUpHour is None and wakeUpMinute is None:
            self._wakeUpHour = 0
            self._wakeUpMinute = 0
        if(self.checkTimeValidity()):
            self._wakeUpHour = wakeUpHour
            self._wakeUpMinute = wakeUpMinute

    def __enter__(self):
        return self
    
    def checkTimeValidity(self, hour, minute):
        if isinstance(hour, int) and isinstance(minute, int):
            if 0 <= hour < HOURS_IN_DAY or 0 <= minute < MINUTES_IN_HOUR:
                return True
            else:
                raise ValueError("Invalid arguments. Hour must be [0 - 23] and minute must be [0 - 59]")  
        else:
            raise ValueError("Invalid arguments. Hour and minute arguments should be integer values")

    def getCurrentHour(self):
        return time.localtime(time.time()).tm_hour
    
    def getCurrentMinute(self):
        return time.localtime(time.time()).tm_min
    
    def resetWakeUpTime(self, wakeUpHour, wakeUpMinute):
        if (self.checkTimeValidity()):
            self._wakeUpHour = wakeUpHour
            self._wakeUpMinute = wakeUpMinute
    
    def timeDiff(self):
        systemTimeMin = time.localtime(time.time()).tm_min
        systemTimeHour = time.localtime(time.time()).tm_hour
    
        if systemTimeHour == self._wakeUpHour:
            if not self._wakeUpMinute < systemTimeMin:
                return (0, self._wakeUpMinute - systemTimeMin)
            else:
                #   wakeUpTime has passed
                return (0,0)
        elif self._wakeUpHour < systemTimeHour:
            #   wakeUpTime has passed
            return (0,0)
        else:
            if self._wakeUpMinute < systemTimeMin:
                """
                Example use case:
                system time: 19:50
                user input: 20:10
                Calculation: 
                Hour: (userInputHour - systemTimeHour) - 1
                Minute: (MINUTES_IN_HOUR - systemTimeMinute) + userInputMinute
                """
                return(self._wakeUpHour - systemTimeHour - 1, (MINUTES_IN_HOUR - systemTimeMin) + self._wakeUpMinute)
            else:
                """
                Example use case:
                system time: 19:10
                user input: 20:50
                Calculation: 
                Hour: (userInputHour - systemTimeHour)
                Minute: (userInputMinute - systemTimeMinute)
                """
                return (self._wakeUpHour - systemTimeHour, self._wakeUpMinute - systemTimeMin)

