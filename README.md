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

***Project budget:***
[Go to Project Budget](https://docs.google.com/spreadsheets/d/1quyFzman1QwOtCFkKcF1BXIo6rP9FyXq6cBiZKglpdo/edit?usp=sharing)

## Requirements
1. Wake-up time should be settable by the user by a HMI of any sort.
2. Upon reaching the pre-set wake-up time, system should keep the leds open at full power, until one of the following occurs:
   + The user manually turns of the system
   + A settable maximum time is reached, and the system still have not been turned off.
3. Regardless of how the system is switched off, it should start at the same time the next day without the user having to re-set it.

## Hardware list
- Raspberry Pi Zero WH
- A Micro USB cable ([not an adapter, a simple micro usb cable is enough](https://www.amazon.de/Amazon-Basics-%C3%9Cbertragungsgeschwindigkeit-vergoldeten-Steckern/dp/B0711PVX6Z/ref=sr_1_1_ffob_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.oIsC04L7KUKZcaw-lx7j0vPDv5CFpfW7NreERp7BZc6JlQkmD5XKjPLTVToS-fuQOOjpgmQdjyxBA9vGx2jewByRtZ_xQOEo75JJB-OdaDF55YGbW7TeFn17kiQDLImTTHTkutg03t65RNl5T0Rqu7nDRxH9-dO7hk3_wmDL1KQJnKLvuL2Sd7cJyBImVsBLUiQWlgFbCqb4XjA-_FbbGZz3ZO-ckXvG3-QfEZEAXPIhQWaQjKDb1rkkR1K5ZJUtFVz6gAREJJcUPM95mlvUCqr5sE-e1I1i-zC6KoI9jHw.Yyja34Ou_4x1LVIVZlJSXKfRVZvegnNSxRRLTg_vdHY&dib_tag=se&keywords=micro+usb+cable&qid=1732449013&s=computers&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1, "Example from amazon"))
- An electronic component kit or set for starting projects. [This one is used in this project](https://www.amazon.de/dp/B01J79YG8G?ref=ppx_yo2ov_dt_b_fed_asin_title, "Amazon link")
- Micro SD card with a proper SD card adapter compatible with your PC





