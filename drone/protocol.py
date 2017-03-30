
import socket
import struct
import time
import threading

S_TYPE = "BBB"


class Server:
    def __init__(self, ip="", port=8080, timeout=-1):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        if (timeout > 0):
            self.sock.settimeout(timeout)

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

    def send(self, data_bytes):
        self.sock.sendto(data_bytes, (self.ip, self.port))

    def send_loop(self):
        '''Send loop is used to regulary send data in a thread'''
        while (self.running):
            self.lock.acquire()
            data_bytes = struct.pack(S_TYPE, *self.data)
            self.lock.release()
            self.send(data_bytes)
            time.sleep(self.interval / 1000.0)

    def update(self, a, b, c):
        '''Update data which is sent'''
        self.lock.acquire()
        self.data = (a, b, c)
        self.lock.release()

    def start(self):
        self.thread.start()

    def stop(self):
        # __del__ wouldn't be called with a thread running
        self.running = False
