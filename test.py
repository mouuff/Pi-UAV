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

client = client.Client(ip="192.168.1.22");

while 1:
	for e in pygame.event.get():
		if e.type == pygame.locals.JOYAXISMOTION:
			x , y = j.get_axis(0), j.get_axis(1)
			print 'x and y : ' + str(x) +' , '+ str(y)
			x += 1
			x /= 2
			x *= 25
			if (x > 25):
				x = 25
			if (x <= 5):
				x = 5
			client.send(x, 0, 0)
			print(x)
			time.sleep(0.1)
