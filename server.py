import socket
import json
import RPi.GPIO as GPIO
from RPIO import PWM

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

servo1 = PWM.Servo()

def set_servo1_angle(angle):
    servo1.set_servo(17, 10*angle + 1680)

def set_lights1(status):
    if(status):
        GPIO.output(3, GPIO.HIGH)
    else:
        GPIO.output(3, GPIO.LOW)

def set_lights2(status):
    if(status):
        GPIO.output(5, GPIO.HIGH)
    else:
        GPIO.output(5, GPIO.LOW)

def set_lights3(status):
    if(status):
        GPIO.output(7, GPIO.HIGH)
    else:
        GPIO.output(7, GPIO.LOW)

def set_lights4(status):
    if(status):
        GPIO.output(8, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.LOW)

def set_lights5(status):
    if(status):
        GPIO.output(10, GPIO.HIGH)
    else:
        GPIO.output(10, GPIO.LOW)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.2.200.164', 1313)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)

    if(data):
        status = json.loads(data)
        set_servo1_angle(status['blinds1'])
        set_lights1(status['lights1'])
        set_lights2(status['lights2'])
        set_lights3(status['lights3'])
        set_lights4(status['lights4'])
        set_lights5(status['lights5'])

