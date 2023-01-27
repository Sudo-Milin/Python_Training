#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 45 :

# Write a program which can filter even numbers in
# a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

number_list = [1,2,3,4,5,6,7,8,9,10]

filtered_list = filter(lambda x: x%2 == 0, number_list)

print(list(filtered_list))
