
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
                pulse = ratio(val, 0, 255, self.MIN_WIDTH, self.MAX_WIDTH)
                if (pulse != self.pulse):
                    self.pulse = pulse
                    self.pwm.ChangeDutyCycle(self.pulse)


class Esc(Servo):
    MAX_WIDTH = 12.0


class Controler:
    STOP = 50

    def __init__(self, sr=26, sl=20, esc=21):
        self.servo_right = Servo(sr)
        self.servo_left = Servo(sl)
        self.esc = Esc(esc)

    def control(self, pitch, roll, throttle):
        self.esc.set(throttle)

        left = ratio(pitch, 0, 255, STOP, 255 - STOP)
        right = ratio(pitch, 255, 0, STOP, 255 - STOP)

        sleft = ratio(roll + left, 0, 255 * 2, 0, 255)
        sright = ratio(roll + right, 0, 255 * 2, 0, 255)

        self.servo_right.set(sright)
        self.servo_left.set(sleft)
