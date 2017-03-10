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

def main():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        pwm_a = GPIO.PWM(18, 100)
        pwm_b = GPIO.PWM(17, 100)
        pwm_c = GPIO.PWM(27, 100)
        pwm_a.start(5)
        pwm_b.start(5)
        pwm_c.start(5)

        server = Server()
        while (1):
                data = server.recv()
                pwm_a.ChangeDutyCycle(data[0])
                pwm_b.ChangeDutyCycle(data[1])
                pwm_c.ChangeDutyCycle(data[2])
                print(data)

if (__name__ == "__main__"):
        main()
