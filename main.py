"""Jaden Brown, 2/26/25, Assignment #6, Program that takes 2 input numbers and does 4 basic arithmatic operations with them"""
a = input("Give me a number:")
b = input("Give me a second number:")
#Storing the 2 input's as values "a" and "b" ^^^
print("Here's some basic arithmatic with your numbers:")
print("")#Wanted a space here so it looked cleaner
print(f'{a} + {b} = {int(a) + int(b)}')
print(f'{a} - {b} = {int(a) - int(b)}')
print(f'{a} / {b} = {int(a) / int(b)}')
print(f'{a} * {b} = {int(a) * int(b)}')
#Lines 7-10 are displaying the arithmatic and their output