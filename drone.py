#!/usr/bin/env python

import RPi.GPIO as GPIO
from drone.protocol import Server
from drone.control import Controller
import socket


def main():
    controller = Controller(sr=26, sl=20, esc=21)
    server = Server(timeout=1)
    while (True):
        try:
            data = server.recv()
            try:
                controller.control(*data)
            except TypeError:
                controller.default()
        except (socket.timeout):
            controller.default()
    # socket.timeout
    # print(data)

if (__name__ == "__main__"):
        main()
