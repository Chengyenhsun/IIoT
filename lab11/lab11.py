import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)


PIR_PIN = 17


GPIO.setup(PIR_PIN, GPIO.IN)


try:
    while True:

        motion_detected = GPIO.input(PIR_PIN)

        if motion_detected:
            print("Motion detected!")
        else:
            print("No motion detected!")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
