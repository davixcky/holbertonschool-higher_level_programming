#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def printer(a, b, op, res):
    print("{0} {2} {1} = {3}".format(a, b, op, res))


if __name__ == "__main__":
    a = 10
    b = 5

    printer(a, b, '+', add(a, b))
    printer(a, b, '-', sub(a, b))
    printer(a, b, '*', mul(a, b))
    printer(a, b, '/', div(a, b))
