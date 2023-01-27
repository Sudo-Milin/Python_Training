#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 19 :

# You are required to write a program to sort the
# (name, age, height) tuples by ascending order
# where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.



list_of_tuples = [] #("Tom",19,80), ("John",20,90), ("Jony",17,93), ("Json",21,85), ("Jony",17,91), ("Json",32,85)]

def sort_list(tuple):
    tuple.sort(key=lambda k: k[2])
    tuple.sort(key=lambda k: k[1])
    tuple.sort(key=lambda k: k[0])
    return tuple

while True:
    user_input = ""
    user_input = (input("Enter tuple: "))
    if user_input == "q":
        break
    else:
        list_of_tuples.append(tuple(data for data in user_input.split(",")))


print(sort_list(list_of_tuples))


# Data types conversion remains



    
