import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

piano = list([523, 589, 659, 698, 784, 880, 988, 1047])
voice = GPIO.PWM(11, 50)
voice.start(50)

try:
    while 1:
        for dc in range(0, 8, 1):
            voice.ChangeFrequency(piano[dc])
            time.sleep(1)

except KeyboardInterrupt:
    pass

voice.stop()
GPIO.cleanup()
