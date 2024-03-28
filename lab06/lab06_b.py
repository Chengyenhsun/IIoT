import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17
LED = 27

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)


def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 34300 / 2
    distance = round(distance, 1)

    return distance


while True:
    try:
        distance = measure_distance()
        print("Distance:", distance, "cm")
        if distance < 10.0:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
    except KeyboardInterrupt:
        break

GPIO.cleanup()
