#!/usr/bin/env python

import RPi.GPIO as GPIO
from protocol import Server

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
