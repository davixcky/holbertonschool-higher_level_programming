#!/usr/bin/python3


def islower(c):
    value = ord(c)
    return value >= 97 and value <= 122


def uppercase(str):
    for letter in str:
        print("{:c}".format(
            ord(letter) - 32 if islower(letter) else ord(letter)), end='')

        print()
