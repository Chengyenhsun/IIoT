import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# 設定 GPIO 的模式為 BCM 模式（Broadcom 腳位編號）。

TRIG = 4
ECHO = 17
# 定義 TRIG 和 ECHO 兩個變量，分別代表超聲波模組的觸發腳位和回聲腳位。
# 可以依自己的腳位去設定

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# 使用 GPIO.setup() 函數設定 TRIG 和 ECHO 的引腳模式，
# TRIG 設為輸出模式，ECHO 設為輸入模式。


def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.5)  # 等待傳感器穩定

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # 初始化pulse_start, pulse_end兩個變數
    pulse_start = time.time()
    pulse_end = time.time()

    # 他這邊等於0的時候代表他現在是高電位，也就是他現在沒有收到回程訊號
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    # 他這邊等於1的時候代表他現在是低電位，也就是他現在收到回程訊號
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # 我們將收到的起始跟結束相減就可以獲得他的時間
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 34300 / 2
    #  乘以聲速(34300 cm/s)
    #  然後因為來回所以要除2
    distance = round(distance, 1)  # 四捨五入到小數點後一位

    return distance


while True:
    try:
        distance = measure_distance()
        print("Distance:", distance, "cm")
        time.sleep(1)
    except KeyboardInterrupt:
        break

GPIO.cleanup()
