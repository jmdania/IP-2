#!/usr/bin/python
"""
To write a CSV file, the .csv file is opened in write mode
and put the file object into csv.writer.
The CSV writer adds a line of list data through the writerow () method.

To read a CSV file, you have to mport the csv module that is in Python. Open the .csv file.
Use the next () function to retrieve the values in order and return them.
"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

import csv

def write_primes(l, file_name):
    """the function read a list of prime numbers and a csv file name as parameters,
    write the number in the list to the csv file

        Args:
           file_name (list): input file name.
           l (int): input list.
        Returns:
           file: output file.
        Raises:
           IOError: io error.
        Examples:
           >>> write_primes(prime, 'output.csv')
        """
    w_file = open(file_name, 'w')
    w_csv = csv.writer(w_file)
    w_csv.writerow([l])

def read_primes(file_name):
    '''it reads an integer number parameter and returns a list containing prime numbers.


       Args:
           file_name (str): intput file name.

       Returns:
           list: list of integers

       Raises:
           IOError: io error.

       Examples:
           >>> list = read_primes('output.csv')

       '''
    r_file = open(file_name, 'r')
    return r_file.__next__()
