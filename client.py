#!/usr/bin/env python2

import socket
import struct
import time

S_TYPE = "BBB"

class Client:
	def __init__(self, ip="raspberrypi", port=8080):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	def send(self, a, b, c):
		data = struct.pack(S_TYPE, a, b, c)
		self.sock.sendto(data, (self.ip, self.port))

def main():
	client = Client();
	x = 0
	while (1):
                data = raw_input(": ")
                esc, s1, s2 = data.split(" ")
                client.send(int(esc), int(s1), int(s2))
		time.sleep(0.1)

	

if (__name__ == "__main__"):
	main()
