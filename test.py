#!/usr/bin/env python

import pygame
from pygame import locals
from drone.protocol import Client

def main():
    client = Client("127.0.0.1")
    client.start()

    x = 0
    while (1):
        data = raw_input(": ")
        esc, s1, s2 = data.split(" ")
        client.update(int(esc), int(s1), int(s2))

if (__name__ == "__main__"):
    main()
