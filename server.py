#!/usr/bin/env python

import RPi.GPIO as GPIO
from drone.protocol import Server
from drone.control import Controler

def main():
        GPIO.setmode(GPIO.BCM)
        controler = Controler()

        server = Server()
        while (True):
                data = server.recv()
                controler.control(*data)
                print(data)

if (__name__ == "__main__"):
        main()
