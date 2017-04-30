
import socket
import struct
import time
import threading

S_TYPE = "BBB"
DEFAULT_PORT = 8080

class Server:
    def __init__(self, ip, port, timeout=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))
        self.sock.settimeout(timeout)

    def recv(self, size):
        return self.sock.recv(size)


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data_bytes):
        self.sock.sendto(data_bytes, (self.ip, self.port))


class ControlServer(Server):
    def __init__(self, ip="", port=DEFAULT_PORT, timeout=None):
        Server.__init__(self, ip, port, timeout)
    
    def recv(self):
        data = Server.recv(self, struct.calcsize(S_TYPE))
        return struct.unpack(S_TYPE, data)


class ControlClient(Client):
    def __init__(self, ip, port=DEFAULT_PORT, interval=50):
        '''Class used to send data regulary in a thread'''
        Client.__init__(self, ip, port)
        self.to_send = (0, 0, 0)
        self.interval = interval
        self.thread = threading.Thread(target=self.send_loop)
        self.thread.daemon = True
        self.lock = threading.Lock()
        self.running = False

    def send_loop(self):
        '''Send loop is used to regulary send data in a thread'''
        while self.running:
            with self.lock:
                data_bytes = struct.pack(S_TYPE, *self.to_send)
            Client.send(self, data_bytes)
            time.sleep(self.interval / 1000.0)

    def update(self, to_send):
        '''Update data which is sent'''
        with self.lock:
            self.to_send = to_send

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        # __del__ wouldn't be called with a thread running
        self.running = False


def test():
    s = ControlServer()
    while (True):
        print s.recv()

if (__name__ == '__main__'):
    test()
