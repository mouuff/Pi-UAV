#!/usr/bin/env python

import pygame
from pygame import locals
from drone.protocol import Client
from drone.misc import ratio
import time

pygame.init()

pygame.joystick.init()

try:
    j = pygame.joystick.Joystick(0)
    j.init()
    print('Enabled joystick: ' + j.get_name())
except pygame.error:
    print('no joystick found.')

client = Client("raspberrypi", interval=50)
client.start()

while 1:
    for e in pygame.event.get():
        if e.type == pygame.locals.JOYAXISMOTION:
            x, y, z = j.get_axis(0), j.get_axis(1), j.get_axis(2)
            # controls = [x, y, throttle]
            print("%f %f %f" % (x, y, z))
            pitch = ratio(x, -1, 1, 0, 255)
            roll = ratio(y, -1, 1, 0, 255)
            throttle = ratio(z, 1, -1, 0, 255)
            client.update((roll, pitch, throttle))
