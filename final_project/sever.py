import socket
import RPi.GPIO as GPIO
import time
import os
import cv2
# vim: set fileencoding=utf-8 :
# led_pin = 21
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


def take_picture():
    # Create directory if it doesn't exist
    output_dir = "aunt_chen"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # 使用cv2.VideoCapture(0)來設置攝像頭
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return

    # 從攝像頭中讀取畫面
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        return


    timestamp = time.strftime('%Y%m%d%H%M%S')
    filename = os.path.join(output_dir, f'bad_{timestamp}.jpg')
    # 將畫面儲存為圖片
    cv2.imwrite(filename, frame)

    # 釋放攝像頭資源
    cap.release()
    cv2.destroyAllWindows()

    print("Call Aunt Chen !!!")


def control_led(state, ):
    
    if state == "yes":
        print("Yes!")
        GPIO.output(15, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(15, GPIO.LOW)
    elif state == "no":
        # 呼叫拍照函數
        take_picture()
        print("No!")
        voice = GPIO.PWM(11,70)
        voice.start(70)
        GPIO.output(13, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(13, GPIO.LOW)
        voice.stop()
    else:
        pass

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("192.168.1.64", 8887))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()


while True:
    try:
        data = client_socket.recv(1024)
        if data:
            command = data.decode().strip()
            control_led(command)
    except KeyboardInterrupt:
        break

client_socket.close()
server_socket.close()
GPIO.cleanup()