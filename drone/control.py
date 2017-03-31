
import RPi.GPIO as GPIO
from .misc import ratio


class Servo:
    FREQ = 50
    MAX_WIDTH = 12.0
    MIN_WIDTH = 1.0

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.pulse = 0
        self.pwm = GPIO.PWM(self.pin, self.FREQ)
        start_width = ratio(0.5, 0, 1, self.MIN_WIDTH, self.MAX_WIDTH)
        self.pwm.start(self.pulse)

    def set(self, val):
        '''val between 0 and 255'''
        if (val > 255):
            val = 255
        if (val < 0):
            val = 0
        pulse = ratio(val, 0, 255, self.MIN_WIDTH, self.MAX_WIDTH)
        if (pulse != self.pulse):
            self.pulse = pulse
            self.pwm.ChangeDutyCycle(self.pulse)


class Esc(Servo):
    '''Electronic speed controler
    '''
    MIN_WIDTH = 5.0
    MAX_WIDTH = 10.0


class Controler:
    STOP = 60

    def __init__(self, sr, sl, esc):
        '''
        UAV controler
        sr: servo right
        sl: servo left
        esc: electronic speed controler
        '''
        GPIO.setmode(GPIO.BCM)
        self.servo_right = Servo(sr)
        self.servo_left = Servo(sl)
        self.esc = Esc(esc)

    def control(self, pitch, roll, throttle):
        self.esc.set(throttle)
        left = ratio(roll, 0, 255, self.STOP, 255 - self.STOP)
        right = ratio(roll, 255, 0, self.STOP, 255 - self.STOP)

        left += pitch - (255.0 / 2.0)
        right += pitch - (255.0 / 2.0)

        self.servo_right.set(right)
        self.servo_left.set(left)
