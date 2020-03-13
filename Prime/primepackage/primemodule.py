#!/usr/bin/python
# primemodule.py
"""
Code identifies prime numbers through these means:
If s is 1, it is not a prime number
S is prime if there are no numbers that are divisible by numbers 2 to S-1
This code uses if statements and boolean (true or false) to distinguish
said numbers used in the list
"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"


def prime(s):
    """
    This code reads a list of prime numbers and outputs said numbers

      Args:
          prime(s): sets the prime number to s
      Returns:
          Boolean: True or false is returned
      Example:
          >>> if prime(7);
      """
    if (s <= 1):
        return False
    for r in range(2, s):
        if (s % r == 0):
                return False
        return True


def getNPrime(num_1):
    """This portion of the code takes a 100 prime number list
       When the prime value is stored, it is then returned by the list.

        Args:
            num_1 (int): inputs the numbers from the list.
        Returns:
            plist: integer list.
        Example:
            >>> al = getNPrime(25)
    """
    plist = []
    for s in range(num_1):
        if prime(s+1):
            plist.append(s+1)
    return plist
    
