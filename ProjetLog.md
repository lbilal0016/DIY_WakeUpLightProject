# Project Log
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
    




