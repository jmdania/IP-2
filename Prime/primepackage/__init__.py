#!/usr/bin/python
"""
This file lets the user know that the directory is part of a package.
If there is no __init__.py file in the directory, it might not be recognized as a package.
"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

from .primeio import write_primes
from .primeio import read_primes
from .primemodule import getNPrime
