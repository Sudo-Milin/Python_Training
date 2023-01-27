#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 49 :

# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.



number_list = [number for number in range(51)]

squared_list = map(lambda x: x**2, (number for number in number_list if number in range(1,21)))

print(list(squared_list))