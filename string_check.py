#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

old_ppl = 100
young_ppl = 11

def name_check():
    """
    Check the input field.
    Return the string if all character is string.
    Include 'space' character check.
    """
    while True:
        try:
            s = input(">?: ")
            f = float(s)
        except ValueError:
            break
    return s


def string_check():
    """
    Check the input field.
    Return the string, if all characters in the string are alphabetic,
    and there is at least one character.
    """
    y = False
    while y != True:
        s = input(">?: ")
        y = str.isalpha(s)
    return s


def integer_check():
    """
    Check the input field.
    Return the integer, if all characters in the string are digits,
    and there is at least one character.
    """
    x = False
    while x != True:
        i = input(">?: ")
        x = str.isdigit(i)
    ii = int(i)
    return ii

#-------------------------------------------------------------------------------
# Questions
print("What's Your name")
name = name_check()


print("How old are you")
age = integer_check()

if age > old_ppl:
    print("Ha! Ha! And playing with the computer :-)\n")
elif age < young_ppl:
    print("You are so young. :-)\n")


print("What is your favorite color")
colo = string_check()


print("\nYour name is: " + str(name),"\nYour age is: " + str(age),"\nYour favorite color is: " + str(colo))
print("\nBye. Bye.\n")
