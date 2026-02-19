#!/usr/bin/env python3

def multiplication_table(num=None):
    if num is None:
        num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

if __name__ == "__main__":
    print(multiplication_table())