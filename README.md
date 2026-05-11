# IoT26-HW03: Motion Detection Photo Capture

## Project Description
This project captures a photo when motion is detected.
A PIR motion sensor detects movement and the Raspberry Pi Camera takes a picture automatically.

## Hardware Components
- Raspberry Pi 5
- Raspberry Pi Camera Module
- PIR motion sensor
- Push button
- Breadboard
- Jumper wires

## Circuit Connection
- PIR sensor OUT: GPIO 4
- PIR sensor VCC: 5V
- PIR sensor GND: GND
- Button: GPIO 2 and GND

## Source Code
The Python code uses gpiozero and Picamera2.
When motion is detected, the camera captures a photo and saves it in the motion_photos folder.
The button is used to stop the program.

## RPI working




https://github.com/user-attachments/assets/5a973e34-4f4d-46ad-870e-7288396f45f6




<img width="3024" height="4032" alt="KakaoTalk_20260510_210825208" src="https://github.com/user-attachments/assets/7d38c235-f300-4f14-91b8-d9ddb36efc61" />

## IDE
<img width="2866" height="1709" alt="스크린샷 2026-05-10 204415" src="https://github.com/user-attachments/assets/b8229ddd-6aed-44fc-9c15-cc010ca48aae" />
