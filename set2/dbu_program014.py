#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 14 :

# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

def count(sentence):
    upper = 0
    lower = 0
    words = str(sentence).split()
    for word in words:
        for letter in word:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
    return(f"Upper Case: {upper}\nLower Case: {lower}")

user_input = input("Enter your sentence: ")

print(count(user_input))