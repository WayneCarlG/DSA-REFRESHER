#!/usr/bin/env python3

def even_or_odd(num=None):
    if num is None:
        num = int(input("Enter a number: "))
    if num % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    print(even_or_odd())