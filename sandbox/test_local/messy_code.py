"""
Module Description:
This module contains a function to check if a number is between 0 and 100 (inclusive).
"""

# Renamed constant to follow UPPER_CASE naming style
MAX_VALUE = 100

def f(z):
    """
    Returns True if z is between 0 and 100 (inclusive), False otherwise.

    Args:
        z (int): The number to check.

    Returns:
        bool: True if z is between 0 and 100, False otherwise.
    """
    return 0 <= z <= MAX_VALUE

# Add a newline at the end of the file to fix the C0304 error
