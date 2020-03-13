#!/usr/bin/python
# __init__.py
"""
This file lets the user know that the directory is part of a package.
The package will be invalid if there is no __init__.py file.
"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

from primepackage.primemodule import getNPrime
from primepackage.primeio import wprimes
from primepackage.primeio import rprimes
