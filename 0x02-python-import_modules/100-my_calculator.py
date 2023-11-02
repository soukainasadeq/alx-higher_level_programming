#!/usr/bin/python3
"""Author: Soukaina Sadeq"""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    arr = ['*', '+', '-', '/']
    if sys.argv[2] not in arr:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] is arr[1]:
        print("{} {} {} = {}".format(a, arr[1], b, add(a, b)))
    elif sys.argv[2] is arr[2]:
        print("{} {} {} = {}".format(a, arr[2], b, sub(a, b)))
    elif sys.argv[2] is arr[0]:
        print("{} {} {} = {}".format(a, arr[0], b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, arr[3], b, div(a, b)))
