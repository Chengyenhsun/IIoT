import socket
import RPi.GPIO as GPIO
import time
# vim: set fileencoding=utf-8 :
# led_pin = 21
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


def control_led(state):
    
    if state == "yes":
        print("Yes!")
        GPIO.output(15, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(15, GPIO.LOW)
    elif state == "no":
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
server_socket.bind(("192.168.1.64", 8888))
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