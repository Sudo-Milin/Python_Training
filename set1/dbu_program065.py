#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 65:

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.


def func(n):
    if n == 0:
        return 0
    else:
        return func(n-1)+100

user_input = int(input("Enter a number: "))
if user_input == 0:
    print(0)
else:
    print(func(user_input))