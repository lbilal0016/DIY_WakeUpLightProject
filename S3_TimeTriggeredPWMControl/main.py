import sys
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/config')
sys.path.append('/home/levent/Desktop/Project/DIY_WakeUpLightProject/10_Libraries')
from project_constants import *
from TimeLibrary import *

def main():
    with ClassName(ClassArgs) as myClass:
        try:
            while True:
                #   Your main loop here
                

        except KeyboardInterrupt:
            print("\nProgram terminated ...")

if __name__ == "__main__":
    main()