#!/usr/bin/env python3

import socket
import struct

S_TYPE = "BBB"

class Client:
	def __init__(self, ip="127.0.0.1", port=8080):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	def send(self, a, b, c):
		data = struct.pack(S_TYPE, a, b, c)
		self.sock.sendto(data, (self.ip, self.port))

def main():
	client = Client();
	client.send(25, 50, 100)
	client.send(100, 10, 44)
	

if (__name__ == "__main__"):
	main()
