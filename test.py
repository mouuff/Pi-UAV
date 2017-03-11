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

client = client.Client(ip="raspberrypi");

def joy2servo(val):
	val = int(((val + 1) / 2) * 255)
	if (val == 0):
		val += 1
	return (val)

while 1:
	for e in pygame.event.get():
		if e.type == pygame.locals.JOYAXISMOTION:
			x , y = j.get_axis(0), j.get_axis(1)
			print 'x and y : ' + str(x) +' , '+ str(y)
			val = joy2servo(x)
			client.send(val, 0, 0)
			print(val)
			time.sleep(0.1)
