import RPi.GPIO as GPIO
import sys
from datetime import datetime, timedelta
import time
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
from project_constants import *


MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

class wakeupTimeHourAndMinute():
    def __init__(self, wakeUpHour=None, wakeUpMinute=None):
        if wakeUpHour is None and wakeUpMinute is None:
            self._wakeUpHour = 0
            self._wakeUpMinute = 0
            self._returnHourMinute.minute = 0

        elif isinstance(wakeUpHour, int) and isinstance(wakeUpMinute, int):
            if wakeUpHour < HOURS_IN_DAY or wakeUpMinute < MINUTES_IN_HOUR:
                self._wakeUpHour = wakeUpHour
                self._wakeUpMinute = wakeUpMinute
            else:
                raise ValueError("Invalid arguments. Hour must be [0 - 23] and minute must be [0 - 59]")    
        else:
            #   class arguments are invalid
            raise ValueError("Invalid arguments. Hour and minute arguments should be integer values")

    def getCurrentHour(self):
        return time.localtime(time.time()).tm_hour
    
    def getCurrentMinute(self):
        return time.localtime(time.time()).tm_min
    
    def resetWakeUpTime(self, wakeUpHour, wakeUpMinute):
        if isinstance(wakeUpHour, int) and isinstance(wakeUpMinute, int):
            if wakeUpHour < HOURS_IN_DAY or wakeUpMinute < MINUTES_IN_HOUR:
                self._wakeUpHour = wakeUpHour
                self._wakeUpMinute = wakeUpMinute
            else:
                raise ValueError("Invalid arguments. Hour must be [0 - 23] and minute must be [0 - 59]")  
        else:
            raise ValueError("Invalid arguments. Hour and minute arguments should be integer values")
    
    def timeDiff(self, hourInput, minuteInput):
        if not (isinstance(hourInput, int) and isinstance(minuteInput, int)):
            raise ValueError("Invalid arguments. Hour and minute arguments should be integer values")
        if not (0 <= hourInput < HOURS_IN_DAY and 0 <= minuteInput < MINUTES_IN_HOUR):
            raise ValueError("Invalid arguments. Hour must be [0 - 23] and minute must be [0 - 59]")  
        
        systemTimeMin = time.localtime(time.time()).tm_min
        systemTimeHour = time.localtime(time.time()).tm_hour
    
        if systemTimeHour == hourInput:
            if not minuteInput < systemTimeMin:
                return (0, minuteInput - systemTimeMin)
            else:
                #   wakeUpTime has passed
                return (0,0)
        elif hourInput < systemTimeHour:
            #   wakeUpTime has passed
            return (0,0)
        else:
            if minuteInput < systemTimeMin:
                """
                Example use case:
                system time: 19:50
                user input: 20:10
                Calculation: 
                Hour: (userInputHour - systemTimeHour) - 1
                Minute: (MINUTES_IN_HOUR - systemTimeMinute) + userInputMinute
                """
                return(hourInput - systemTimeHour - 1, (MINUTES_IN_HOUR - systemTimeMin) + minuteInput)
            else:
                """
                Example use case:
                system time: 19:10
                user input: 20:50
                Calculation: 
                Hour: (userInputHour - systemTimeHour)
                Minute: (userInputMinute - systemTimeMinute)
                """
                return (hourInput - systemTimeHour, minuteInput - systemTimeMin)

