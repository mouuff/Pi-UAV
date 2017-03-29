#!/usr/bin/env python

import RPi.GPIO as GPIO
from drone.protocol import Server
from drone.control import Servo

def main():
        GPIO.setmode(GPIO.BCM)
        servo_a = Servo(18)
        servo_b = Servo(17)
        servo_c = Servo(27)
        # 17 / 27

        server = Server()
        while (1):
                data = server.recv()
                servo_a.rotate(data[0])
                servo_b.rotate(data[1])
                servo_c.rotate(data[2])
                print(data)

if (__name__ == "__main__"):
        main()
