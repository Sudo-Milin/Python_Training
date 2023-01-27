#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 21 :

# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program
# to compute the distance from current position after a sequence
# of movement and original point. If the distance
# is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

def check_position(moves): 
    co_od = [0,0]
    for tuple in moves:
        if tuple[0] == "up":
            co_od[0]+=int(tuple[1])
        elif tuple[0] == "down":
            co_od[0]-=int(tuple[1])
        elif tuple[0] == "right":
            co_od[1]+=int(tuple[1])
        elif tuple[0] == "left":
            co_od[1]-=int(tuple[1])
    result = (((co_od[0])**2)+((co_od[1])**2))**(0.5)
    return round(result)

list_of_moves = []
while True:
    user_input = ""
    user_input = (input("Enter moves: "))
    if user_input == "q":
        break
    else:
        list_of_moves.append(tuple(move for move in user_input.split(",")))

print(check_position(list_of_moves))