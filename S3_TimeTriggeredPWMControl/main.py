import sys
import ast

sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/10_Libraries')

from project_constants import *
from TimeLibrary import *
from PWM import *

def main():
    with wakeUpTimeHourAndMinute(None, None) as alarmClock, LEDPWM(PWM_PIN_GPIO) as ledController:
        try:
            wakeUpTimeSet = False
            while True:
                if wakeUpTimeSet is not True:
                    wakeUpTime = input("Enter your desired wake-up time (hh,mm) or exit using 'q'\n")
                
                    if wakeUpTime.lower() == 'q':
                        print("\nProgram terminated ...")
                        return

                    try:
                        wakeUpTimeTuple = ast.literal_eval(wakeUpTime)
                        if isinstance(wakeUpTimeTuple, tuple) and len(wakeUpTimeTuple) == 2:
                            wakeUpHour, wakeUpMinute = wakeUpTimeTuple
                            if(alarmClock.checkTimeValidity(wakeUpHour, wakeUpMinute)):
                                alarmClock.resetWakeUpTime(wakeUpHour, wakeUpMinute)
                                wakeUpTimeSet = True
                                print(f"Wake-up time set to: {wakeUpHour:02d}:{wakeUpMinute:02d}")
                            #   Else case is already handled in checkTimeValidity method

                    except (ValueError, SyntaxError):
                        print("Error: Invalid input format. Please enter a tuple in the format (hh, mm) or enter q to exit.")
                
                    timeRemaining = alarmClock.timeDiff()
                    print(f"Current system time: {alarmClock.getCurrentHour():02d}:{alarmClock.getCurrentMinute():02d}")
                    print(f"Time remaining for wake-up alarm: {timeRemaining[0]:02d}:{timeRemaining[1]:02d}")
                timeRemaining = alarmClock.timeDiff()
                if timeRemaining[0] == 0:
                    #   Wake-up hour has come
                    if timeRemaining[1] <= DAWN_TO_SUNRISE_MIN:
                        #   Wake-up minute is approaching
                        dutyCycle = ledController.calculateDutyCycleFromTimeRemaining(timeRemaining[1])
                        debugCounter = 0
                        if debugCounter == 10000 or debugCounter == 0:
                            print(f"Time remaining for wake-up: {timeRemaining[1]:02d} min | PWM Duty Cycle = {dutyCycle}")
                            debugCounter = 0
                        ledController.set_brightness(dutyCycle)
                        debugCounter += 1

        except KeyboardInterrupt:
            print("\nProgram terminated ...")

if __name__ == "__main__":
    main()