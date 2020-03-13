#!/usr/bin/python
# generate.py
"""A simple program that generates a list of prime numbers and places them into a separate csv file.
   Each file plays an important part in producing aforementioned output file.

"""
__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

from primepackage import *


def main():
    """This will simply generate 100 prime numbers into a list and then outputs them into the csv file.

    Args:
        a1: reads the csv file
    Returns:
        output: string of prime number list
    """
    primes = getNPrime(100)

    wprimes(primes, 'output.csv')

    al = rprimes('output.csv')

    print(al)


if __name__ == '__main__':
    main()
