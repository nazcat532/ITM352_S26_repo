# Handy library of mathematical functions
# Name: Nazca
# Date: 2026-01-27

def midpoint(num1, num2):
    """Calculate the midpoint between two numbers"""
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    """Calculate the square root of a number """
    if number < 0:
        return None
    return number ** 0.5

def exponent ( base, exp ):
    """Calculate the exponentiation of a base to a given exponent"""
    result = base ** exp
    rounded_result = round(result, precision)
    return rounded_result