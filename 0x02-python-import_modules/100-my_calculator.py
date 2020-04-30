#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv[1:]
argc = len(argv)


def controller(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    else:
        print('unknown operator. available operators: +, -, * and /')
        exit(1)


if __name__ == "__main__":
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[0])
    b = int(argv[2])

    op = argv[1]

    res = controller(a, b, op)
    print('{} {} {} = {}'.format(a, op, b, res))
