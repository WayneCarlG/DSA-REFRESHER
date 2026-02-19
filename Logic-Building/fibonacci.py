#!/usr/bin/env python3

def fibonacii(num):
    if num < 0:
        return "Please enter a non-negative integer."
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacii(num - 1) + fibonacii(num - 2)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(fibonacii(num))