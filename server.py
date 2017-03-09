#!/usr/bin/env python3

import socket
import struct

S_TYPE = "BBB"

class Server:
	def __init__(self, port=8080, ip=""):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip, port))
	
	def recv(self):
		data = self.sock.recv(struct.calcsize(S_TYPE))
		res = struct.unpack("BBB", data)
		return(res)

def main():
	server = Server()
	data = server.recv()
	print(data)
	
	data = server.recv()
	print(data)

if (__name__ == "__main__"):
	main()
