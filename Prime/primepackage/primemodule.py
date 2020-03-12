#!/usr/bin/python
"""
This code uses the following rules to determine prime numbers:
If N is 1, then it is not prime.
N is a prime number if there is no single number divided by the natural numbers from 2 to N-1.

"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"


def is_prime(n):
    """
    read a natural number, return True if it is a prime number, return False otherwise
    '''

      Args:
          is_prime(int): input number to n
      Returns:
          Boolean: it returns either true or false.
      Raises:
          IOError: io error.
      Examples:
          >>> if is_prime(6);
      '''
      """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for m in range(2, n // 2 + 1):
            if n % m == 0:
                return False
        return True


def getNPrime(num):
    """It receives a list of 100 prime numbers
           The prime value is stored in the list and returned it.

        Args:
            num (int): input numbers

        Returns:
            list: a list of integers.

        Raises:
            IOError: io error.

        Examples:
            >>> l = getNPrime(40)
    """
    prime_list = []
    first_num = 2
    count = 0

    while count < num:
        if is_prime(first_num):
            prime_list.append(first_num)
            count = count + 1
        first_num = first_num + 1
    return prime_list
    
