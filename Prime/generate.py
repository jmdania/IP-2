#!/usr/bin/python
# generate.py
"""A Python program generating a list of prime numbers and output them into a csv file

"""
__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

from primepackage import *


def main():
    """Generate 100 prime numbers and output it into output.csv file

    """
    primes = getNPrime(100)

    write_primes(primes, 'output.csv')

    l = read_primes('output.csv')

    print(l)


if __name__ == '__main__':
    main()
