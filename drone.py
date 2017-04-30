#!/usr/bin/env python

import RPi.GPIO as GPIO
from drone.protocol import Server
from drone.control import Controler
import socket


def main():
    controler = Controler(sr=26, sl=20, esc=21)
    server = Server(timeout=1)
    while (True):
        try:
            data = server.recv()
            try:
                controler.control(*data)
            except TypeError:
                controler.default()
        except (socket.timeout):
            controler.default()
    # socket.timeout
    # print(data)

if (__name__ == "__main__"):
        main()
