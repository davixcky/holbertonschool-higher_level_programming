#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    res = True

    try:
        print('{:d}'.format(value))
    except (ValueError, TypeError) as err:
        res = False
        print('Exception: {}'.format(err), file=stderr)

    return res
