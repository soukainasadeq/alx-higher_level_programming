#!/usr/bin/python3
def print_last_digit(number):
    mod = abs(number) % 10
    print(f"{mod}", end='')
    return mod
