import RPi.GPIO as GPIO
import time
import tm1637

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 17

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

DIO_PIN = 24
CLK_PIN = 23

GPIO.setup(DIO_PIN, GPIO.OUT)
GPIO.setup(CLK_PIN, GPIO.OUT)
Display = tm1637.TM1637(23, 24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)


def send_data(data):
    for i in range(8):
        GPIO.output(DIO_PIN, data & 0x80)
        GPIO.output(CLK_PIN, True)
        time.sleep(0.000001)
        GPIO.output(CLK_PIN, False)
        data <<= 1


def display_number(number):
    num_str = str(round(number)).zfill(4)  # 将距离值转换为整数，并填充成4位字符串
    Display.Show([int(num_str[0]), int(num_str[1]), int(num_str[2]), int(num_str[3])])


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
    distance = round(pulse_duration * 17150, 1)
    return distance


try:
    while True:
        distance = measure_distance()
        display_number(distance)
        print("Distance:", distance, "cm")
        time.sleep(3)  # 每隔3秒更新一次数据
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
