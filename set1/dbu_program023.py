#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 23 :

# Write a method which can calculate square value of number

# Hints:
# Using the ** operator

def squared(number):
    squared_number = number**2
    return squared_number

while True:
    user_input = (input("Enter a number to square or 'q' to quit: "))
    if user_input == 'q':
        break
    else:
        print(squared(int(user_input)))