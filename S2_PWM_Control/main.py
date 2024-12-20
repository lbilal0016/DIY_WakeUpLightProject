import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/10_Libraries')
from project_constants import *
from PWM import *

def main():
    with LEDPWM(PWM_PIN_GPIO) as led:
        try:
            while True:
                brightness = input("Enter brightness level (0 - 100) or exit using 'q'\n")

                if brightness.lower() == 'q':
                    print("\nProgram terminated ...")
                    break
                if brightness.isdigit():
                    led.set_brightness(int(brightness))
                else:
                    print("Please enter a valid number (0 - 100) or exit program using 'q'")

        except KeyboardInterrupt:
            print("\nProgram terminated ...")

if __name__ == "__main__":
    main()