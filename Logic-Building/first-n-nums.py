#!/usr/bin/env python3

def sum_first_n_nums(num):
    num = int(input("Enter a number: "))
    if num < 1:
        return
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

if __name__ == "__main__":
    print(sum_first_n_nums(0))