import RPi.GPIO as GPIO
import time
import tm1637

# GPIO23 (Pin 16) <-> CLK
# GPIO24 (Pin 18) <-> DI0

Display = tm1637.TM1637(23, 24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


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


def display_distance(distance):
    # 将距离转换为整数并显示在TM1637上
    distance_int = int(distance)
    Display.Show(
        [
            distance_int // 1000,
            (distance_int // 100) % 10,
            (distance_int // 10) % 10,
            distance_int % 10,
        ]
    )


try:
    while True:
        distance = measure_distance()
        display_distance(distance)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
