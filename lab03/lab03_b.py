import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 50)
pwm.start(0)

try:
    while 1:
        for dc in range(0, 101, 10):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)

        time.sleep(1)

        for dc in range(100, -1, -10):
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
