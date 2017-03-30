#!/usr/bin/env python

import RPi.GPIO as GPIO
from drone.protocol import Server
from drone.control import Controler


def main():
        GPIO.setmode(GPIO.BCM)
        controler = Controler(sr=26, sl=20, esc=21)

        server = Server()
        while (True):
                data = server.recv()
                # socket.timeout
                controler.control(*data)
                print(data)

if (__name__ == "__main__"):
        main()
