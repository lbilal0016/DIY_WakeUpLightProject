# Project Log
## 15.12.2024
### Log
+ Methods to drive a regular IKEA light bulb was researched
+ Necessary material to realise PWM control on a light bulb was researched

### Method for driving a light bulb using PWM output of control board
To control the brightness of a regular light bulb, an AC Light dimmer circuit is required. That kind of circuit can be a DIY Project on its own, but in this project it will be purchased as material.

[This circuit is compatible with raspberry pi boards](https://www.amazon.de/RobotDYN-PWM-Programmierbarer-Lichtdimmer-110/dp/B07KDNMTSF "RobotDYN PWM Ac Programmierbarer Lichtdimmer")

### Required material
+ [An AC power cable, similar to this one](https://www.bauhaus.info/gurtwickler/wir-elektronik-anschlusskabel-8er-serie/p/29222289?utm_source=google&utm_medium=ssa&utm_id=17397527735_150014389570&cid=SSAGoo17397527735_150014389570&gad_source=1&gclid=CjwKCAiAmfq6BhAsEiwAX1jsZzUjwetNE-81AkUrYsTepOIlx-24dFoZCR0-ilMvJqERUiIIw3HjVhoCPXkQAvD_BwE "Anschlusskabel mit Stecker")
+ [A light bulb socket, similar to this one. (Note that the socket on your lamp may also be modified to achieve the same goal)](https://www.bauhaus.info/lampenfassungen/voltomat-lampenfassung-mit-glattmantel/p/12209139, "Voltomat Lampenfassung mit Glattmantel")
+ [AC light dimmer module](https://www.ebay.de/itm/165592423044?chn=ps&_ul=DE&norover=1&mkevt=1&mkrid=707-166974-037691-2&mkcid=2&mkscid=101&itemid=165592423044&targetid=2274951440814&device=c&mktype=pla&googleloc=9042523&poi=&campaignid=21875900095&mkgroupid=166776655901&rlsatarget=pla-2274951440814&abcId=10084851&merchantid=5453901904&geoid=9042523&gad_source=1&gclid=CjwKCAiAmfq6BhAsEiwAX1jsZ1l6eYhq0Vgrkq0s3rit1QIcjD6vLQpmgmHxeN3VVnNn9mRIzGA1vRoC1fkQAvD_BwE "Ebay link")

## 08.12.2024
### Log
+ Time library was developed as a new class.
+ PWM functions were also enhanced to a new class

####    Bugfix: PWM Powered LED brightness control caused flickering

PWM Control was successful, but there was an annoying flickering in LED. This caused by the RPi library which used software control for PWM modulation. To solve this problem, RPi was replaced by pigpio, which uses hardware control for pwm modulation. [pigpio library](https://abyz.me.uk/rpi/pigpio/python.html)

Unfortunately, pigpio does not support board pin numbering, so the pin number for pwm output was replaced by GPIO number. The current board numbering for Raspberry Pi Zero WH can be checked from [this link](https://pinout.xyz/pinout/pin12_gpio18/).

Also, to start pigpio Daemon, which is an interface for pigpio library, following commands should be entered:

Start pigpio Daemon

        sudo pigpiod
Validate that pigpio Daemon is running

        ps aux | grep pigpiod

Automatically start pigpio Daemon during startup

        sudo systemctl enable pigpiod
        sudo systemctl start pigpiod

## 24.11.2024
### Log
+ Board setup complete: Headless setup. OS and network configuration settings were made using Raspberry Pi Imager. For support, the following video is really helpful: [The New Method to Setup Raspberry Pi Zero (2023 Tutorial)](https://www.youtube.com/watch?v=yn59qX-Td3E&list=PLWmGmAzSVdakg7OxVuu71WXp99VclC1tY, "Headless setup").
+ First getting started project was created: a blinking led.
+ Second step (S2) was completed: PWM modulated brightness control.

### Environment preperation after initialisation
1. Update the packages:
        
        sudo apt update
        sudo apt upgrade -y
        sudo apt autoremove -y
        sudo reboot
2. Installing git:

        sudo apt install git -y
        git --version
        git config --global user.name "username"
        git config --global user.email "user@email.com"
        git config --global credential.helper store
        ##  user token will be saved after the first push
3. Development tools:

        sudo apt install python3 python3-pip -y
        sudo apt install python3-rpi.gpio

        sudo apt install build-essential -y
        sudo raspi-config
    >Interface options -> Activate "I2C" and "SPI" options

## Project start: 17.11.2024

### Log
+   Initial requirements to the project have been defined
+   Initial hardware requirements have been defined
+   Roadmap have been defined

### Roadmap

1. Essential hardware will be supplied
2. Warm-up with the development environment

    *   Initialising the development environment
    *   Connecting to the development environment remotely
    *   Setting up the python interpreter
    *   Fetching development libraries
  
3. Initiating basic functionality:
   
   * Powering LED strips
   * PWM regulation

4.  Development of more advanced functions


    




