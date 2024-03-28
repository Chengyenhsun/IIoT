import RPi.GPIO as GPIO
import time

# GPIO SETUP
sound = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)


def check_sound():
    if GPIO.input(sound):
        print("Sound Detected!")
    else:
        print("Sound not Detected!")


# infinite loop
while True:
    check_sound()
    time.sleep(1)

GPIO.cleanup()
