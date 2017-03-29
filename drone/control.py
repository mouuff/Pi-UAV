
import RPi.GPIO as GPIO

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
