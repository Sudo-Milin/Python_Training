#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 20 :

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

class Divisible:
    def __init__(self, number):
        self.number = number

    def divisible(self):
        for i in range(1,self.number+1):
            if i%7 == 0:
                yield i


user_input = int(input("Enter a number: "))

div_obj = Divisible(user_input)
for number in div_obj.divisible():
    print(number)