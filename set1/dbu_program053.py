#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 53 :

# Define a class named Rectangle which can be
# constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.




class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        self.result = self.width * self.length
        print(f"The area of rectangle is {self.result}")
    

rect_obj = Rectangle(43,74)
rect_obj.calculate_area()