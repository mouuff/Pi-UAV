import pygame
from pygame import locals
import client
import time

pygame.init()

pygame.joystick.init()

try:
	j = pygame.joystick.Joystick(0)
	j.init()
	print 'Enabled joystick: ' + j.get_name()
except pygame.error:
	print 'no joystick found.'

client = client.Client();

def joy2servo(val, minv = 70, maxv = 180):
	val = int(((val + 1) / 2) * 255)
	if (val > maxv):
		val = maxv
	if (val < minv):
		val = minv
	return (val)

while 1:
	for e in pygame.event.get():
		if e.type == pygame.locals.JOYAXISMOTION:
			x , y, throttle = j.get_axis(0), j.get_axis(1), j.get_axis(2)
			sx = joy2servo(x)
			esc = joy2servo(throttle, 1, 255)
			client.send(sx, 0, esc)
			time.sleep(0.1)
