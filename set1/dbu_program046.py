#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.


list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

squared_numbers = map(lambda number: number**2, list_of_numbers)

print(list(squared_numbers))

