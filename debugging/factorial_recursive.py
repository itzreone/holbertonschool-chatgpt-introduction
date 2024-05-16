#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number using recursion.

    Parameters:
    - n: An integer representing the number for which the factorial is to be calculated.

    Returns:
    An integer representing the factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the command-line argument and convert it to an integer
f = factorial(int(sys.argv[1]))

# Print the factorial result
print(f)
