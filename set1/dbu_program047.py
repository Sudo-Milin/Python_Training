#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 47 :

# Write a program which can map() and filter() to make
# a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.



number_list = [1,2,3,4,5,6,7,8,9,10]

filtered_list = filter(lambda x: x%2 == 0, number_list)
squared_numbers = map(lambda number: number**2, filtered_list)

print(list(squared_numbers))

