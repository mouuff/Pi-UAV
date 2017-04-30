#!/usr/bin/env python

from drone.protocol import Client


def main():
    client = Client("127.0.0.1")
    client.start()

    x = 0
    while (1):
        string = raw_input(": ")
        pitch, roll, throttle = map(int, string.split(" "))
        client.update((pitch, roll, throttle))

if (__name__ == "__main__"):
    main()
