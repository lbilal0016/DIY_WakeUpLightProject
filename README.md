# DIY Wakeup-Light Project
This project is about realising an artificial sunlight (wake-up light) system by yourself at home

## About the project
***Aim of the project:*** Design of an artificial sunlight that can be set to a specific wake-up time. The system should begin to power up the LEDs gradually, resulting in a gradual illumination of the room. At the scheduled wake-up time, the LEDs should be at full power, simulating a sunrise.

***Predicted list of materials:***

+ A development board
+ A user interface, prefably a led screen to indicate the set wake-up time
+ A switch button or a similar mechanism for the user to give the target wake-up input
+ Led strips
+ Depending on the board, a pwm module
+ Power source, prefably an adapter

## Requirements
1. Wake-up time should be settable by the user by a HMI of any sort.
2. Upon reaching the pre-set wake-up time, system should keep the leds open at full power, until one of the following occurs:
   + The user manually turns of the system
   + A settable maximum time is reached, and the system still have not been turned off.
3. Regardless of how the system is switched off, it should start at the same time the next day without the user having to re-set it.





