#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 60 :

# Write a program which accepts a sequence
# of words separated by whitespace as input to print
# the words composed of digits only.

# Example:
# If the following words is given as input to the program:

# 2 cats and 3 dogs.

# Then, the output of the program should be:

# ['2', '3']

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

def extract_number(sequence):
    result = []
    content_of_sequence = sequence.split(" ")
    for word in content_of_sequence:
        if word.isdigit():
            result.append(word)
    return result


user_input = input("Enter the sequence: ")
print(extract_number(user_input))