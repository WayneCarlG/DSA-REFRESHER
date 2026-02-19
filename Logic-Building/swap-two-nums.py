#!/usr/bin/env python3

def swap_two_nums(num1, num2):
	num1 = int(input("Enter the number to variable a:"))
	num2 = int(input("Enter the number to varible b:"))

	container = num1
	num1 = num2
	num2 = container

	print(f"The num1 = {num1} and num2 = {num2}")

if __name__ == "__main__":
	print(swap_two_nums(num1, num2))   
