import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637

# GPIO23 (Pin 16) <-> CLK
# GPIO24 (Pin 18) <-> DI0

Display = tm1637.TM1637(23, 24, tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.SetBrightnes(1)


def countdown_timer(seconds):
    for i in range(seconds, -1, -1):
        if i == 0:
            # 倒计时结束，LED 显示 "0000" 闪烁
            for _ in range(5):  # 闪烁5次
                Display.Show([0, 0, 0, 0])
                time.sleep(0.5)
                Display.Clear()
                time.sleep(0.5)
        else:
            # 更新 LED 显示为剩余时间
            Display.Show(
                [i // 1000, (i // 100) % 10, (i // 10) % 10, i % 10]
            )  # 显示剩余秒数
            time.sleep(1)


def main():
    try:
        while True:
            user_input = input("輸入秒數：")
            if user_input.isdigit() and 1 <= int(user_input) <= 9:
                seconds = int(user_input)
                countdown_timer(seconds)
            else:
                print("請輸入有效數字")
    except KeyboardInterrupt:
        print("結束")
    finally:
        GPIO.cleanup()  # 清理 GPIO


if __name__ == "__main__":
    main()
