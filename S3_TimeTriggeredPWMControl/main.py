import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/10_Libraries')
from project_constants import *
from TimeLibrary import *
import ast

def main():
    with wakeUpTimeHourAndMinute(None, None) as alarmClock:
        try:
            while True:
                wakeUpTime = input("Enter your desired wake-up time (hh:mm) or exit using 'q'\n")
                
                if wakeUpTime.lower() == 'q':
                    print("\nProgram terminated ...")
                    break

                try:
                    wakeUpTimeTuple = ast.literal_eval(wakeUpTime)
                    if isinstance(wakeUpTimeTuple, tuple) and len(wakeUpTimeTuple) == 2:
                        wakeUpHour, wakeUpMinute = wakeUpTimeTuple
                        if(alarmClock.checkTimeValidity(wakeUpHour, wakeUpMinute)):
                            print(f"Wake-up time set to: {wakeUpHour:02d}:{wakeUpMinute:02d}")
                        #   Else case is already handled in checkTimeValidity method
                except (ValueError, SyntaxError):
                    print("Error: Invalid input format. Please enter a tuple in the format (hh, mm) or enter q to exit.")
                
                timeRemaining = alarmClock.timeDiff()
                print(f"Current system time: {alarmClock.getCurrentHour:02d}:{alarmClock.getCurrentMinute:02d}")
                print(f"Time remaining for wake-up alarm: {timeRemaining[0]:02d}:{timeRemaining[1]:02d}")

        except KeyboardInterrupt:
            print("\nProgram terminated ...")

if __name__ == "__main__":
    main()