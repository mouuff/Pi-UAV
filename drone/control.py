
import RPi.GPIO as GPIO
from .misc import ratio

class Servo:
        FREQ = 50
        MAX_WIDTH = 12.0
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

class Esc(Servo):
	MAX_WIDTH = 12

class Controler:
	def __init__(self, sr=26, sl=20, esc=21):
		self.servo_right = Servo(sr)
		self.servo_left = Servo(sl)
		self.esc = Esc(esc)

	def control(self, pitch, roll, throttle):
		self.esc.rotate(throttle)
		sleft = ratio(pitch, 0, 255, 55, 250)
		sright = ratio(pitch, 255, 0, 55, 250)

		sleft = ratio(roll + sleft, 0, 510, 0, 255)
		sright = ratio(roll + sright, 0, 510, 0, 255)
		self.servo_right.rotate(sright)
		self.servo_left.rotate(sleft)
