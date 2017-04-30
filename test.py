#!/usr/bin/env python

from drone.protocol import Client


def main():
    client = Client("127.0.0.1")
    client.start()

    x = 0
    while (1):
        string = raw_input(": ")
        throttle, roll, pitch = string.split(" ")
        data = {
            "pitch": pitch,
            "roll": roll,
            "throttle": throttle
        }
        client.update(data)

if (__name__ == "__main__"):
    main()
