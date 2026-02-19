#!/usr/bin/env python3

def sum_of_squares(num):
    # total_sq = 0
    # if num < 1:
    #     return "Please enter a positive integer."
    # for i in range(1, num + 1):
    #     total_sq += i ** 2
    # return total_sq
    if num == 1:
        return 1
    return sum_of_squares(num - 1) + num ** 2

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(sum_of_squares(num))