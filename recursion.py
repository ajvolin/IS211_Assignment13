#!/usr/bin/python
# -*- coding: utf-8 -*-

"""recursion.py: IS 211 Assignment 13."""

__author__ = 'Adam Volin'
__email__ = 'Adam.Volin56@spsmail.cuny.edu'


def fibonacci(n):
    """Function to get the nth element of the fibonacci sequence."""

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Incorrect spelling in the assignment details, calls properly spelled function
def fibonnaci(n):
    """Function to redirect mispelled function name to correct function."""

    return fibonacci(n)


def gcd(a, b):
    """Function to get the greatest common divisor for two integers."""

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """Function to compare two strings to each other."""

    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
    

def main ():
    """The function that runs when the program is executed."""
    
    print("The 15th element of the fibonacci sequence is {}.".format(fibonacci(15)))
    print("The greatest common divisor of 32 and 96 is {}.".format(gcd(32, 96)))
    print("The result of the string comparison str1 and str2 is {}.".format(compareTo("Testing str1", "Testing str2")))


if __name__ == '__main__':
    main()
