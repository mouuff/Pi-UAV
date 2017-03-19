#!/usr/bin/env python

import RPi.GPIO as GPIO
import socket
import struct

S_TYPE = "BBB"

class Server:
        def __init__(self, port=8080, ip=""):
                self.ip = ip
                self.port = port
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sock.bind((ip, port))

        def recv(self):
                data = self.sock.recv(struct.calcsize(S_TYPE))
                res = struct.unpack("BBB", data)
                return(res)

class Servo:
        FREQ = 100
        MAX_WIDTH = 25.0
        MIN_WIDTH = 1.0

        def __init__(self, pin):
                GPIO.setup(pin, GPIO.OUT)
                self.pwm = GPIO.PWM(pin, self.FREQ)
                self.pwm.start(0)

        def rotate(self, val):
                '''val between 0 and 255'''
                pulse = float(val) / (255.0 / self.MAX_WIDTH)
                if (val > 0 and pulse < self.MIN_WIDTH):
                        pulse = self.MIN_WIDTH
                self.pwm.ChangeDutyCycle(pulse)

def main():
        GPIO.setmode(GPIO.BCM)
        servo_a = Servo(18)
        servo_b = Servo(17)
        servo_c = Servo(27)
        #17 / 27

        server = Server()
        while (1):
                data = server.recv()
                servo_a.rotate(data[0])
                servo_b.rotate(data[1])
                servo_c.rotate(data[2])
                print(data)

if (__name__ == "__main__"):
        main()
