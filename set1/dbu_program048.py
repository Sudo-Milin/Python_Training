#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 48 :

# Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


number_list = [number for number in range(51)]

filtered_list = filter(lambda x: x%2 == 0, number_list)

print(list(number for number in filtered_list if number in range(1,21)))
