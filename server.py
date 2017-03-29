#!/usr/bin/env python

import RPi.GPIO as GPIO
from protocol import Server

def ratio(x, min_x, max_x, new_min, new_max):
	x = float(x)
	if (x < min_x):
		x = min_x
	if (x > max_x):
		x = max_x
	old_range = max_x - min_x
	new_range = new_max - new_min
	if (old_range == 0):
		old_range = 1
	res = ((x - min_x) / old_range) * new_range + new_min
	return (res)

class Servo:
        FREQ = 100
        MAX_WIDTH = 25.0
        MIN_WIDTH = 1.0

        def __init__(self, pin):
                GPIO.setup(pin, GPIO.OUT)
                self.pwm = GPIO.PWM(pin, self.FREQ)
                start_width = ratio(0.5, 0, 1, self.MIN_WIDTH, self.MAX_WIDTH)
                self.pwm.start(0)

        def rotate(self, val):
                '''val between 0 and 255'''
                pulse = ratio(val, 0, 255, self.MIN_WIDTH, self.MAX_WIDTH)
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
