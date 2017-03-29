#!/usr/bin/env python

import socket
import struct
import time
import threading

S_TYPE = "BBB"

class Server:
	def __init__(self, ip="", port=8080):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip, port))

	def recv(self):
		data = self.sock.recv(struct.calcsize(S_TYPE))
		res = struct.unpack("BBB", data)
		return (res)

class Client:
	def __init__(self, ip, port=8080, interval=100):
		self.ip = ip
		self.port = port
		self.data = (0, 0, 0)
		self.interval = interval
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.thread = threading.Thread(target=self.send_loop)
		self.thread.daemon = True
		self.lock = threading.Lock()
		self.running = True

	def send_loop(self):
		while (self.running):
			self.lock.acquire()
			data = struct.pack(S_TYPE, *self.data)
			self.lock.release()
			self.sock.sendto(data, (self.ip, self.port))
			time.sleep(self.interval / 1000)
			
	def update(self, a, b, c):
		self.lock.acquire()
		self.data = (a, b, c)
		self.lock.release()
	
	def start(self):
		self.thread.start()
	
	def stop(self):
		#__del__ wouldn't be called with a thread running
		self.running = False
