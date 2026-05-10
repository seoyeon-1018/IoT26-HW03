from gpiozero import MotionSensor, Button
from picamera2 import Picamera2
from time import sleep
from datetime import datetime
from pathlib import Path
from signal import pause
import sys

# Set PIR motion sensor to GPIO 4
pir = MotionSensor(4)

# Set button to GPIO 2
# One side of the button is connected to GPIO 2
# The other side is connected to GND
button = Button(2, pull_up=True)

# Create a folder to save captured photos
save_dir = Path.home() / "Desktop" / "motion_photos"
save_dir.mkdir(parents=True, exist_ok=True)

# Set up the camera
camera = Picamera2()
camera.configure(camera.create_still_configuration())
camera.start()

print("카메라 준비 중...")
sleep(2)
print("움직임 감지 대기 중...")
print("버튼을 누르면 프로그램이 종료됩니다.")

# Take a photo when motion is detected
def take_photo():
    # Create a file name using the current date and time
    filename = save_dir / f"motion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

    print("움직임 감지됨! 사진 촬영 중...")

    # Capture and save the photo
    camera.capture_file(str(filename))

    print(f"사진 저장 완료: {filename}")

    # Wait for a few seconds to avoid taking too many photos
    sleep(3)

# Stop the program when the button is pressed
def stop_program():
    print("버튼이 눌렸습니다. 프로그램을 종료합니다.")

    # Stop the camera before exiting
    camera.stop()
    sys.exit()

# Run take_photo() when motion is detected
pir.when_motion = take_photo

# Run stop_program() when the button is pressed
button.when_pressed = stop_program

try:
    # Keep the program running
    pause()

except KeyboardInterrupt:
    print("Ctrl + C 입력됨. 프로그램을 종료합니다.")

    # Stop the camera safely
    camera.stop()