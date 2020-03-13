#!/usr/bin/python
# primeio.py
"""
In order to generate a CSV file, it must be opened and then placed into the csv's writer method.

To read a CSV file, you have to import the csv module that is in Python. Open the .csv file.
The __next__() function will retrieve and return the output in the csv file.
"""

__author__ = "Jason Dania"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "jmdania@valdosta.edu"
__status__ = "Complete"

import csv

def wprimes(al, fname):
    """This reads a prime number and the csv file's name then incorporates
    each number in the list into the output file.

        Args:
           file: incorporates and writes the csv's file name.
           al (int): This is for the list.
        Returns:
           outfile: This is for the output csv file.
        Example:
           >>> wprimes(prime, 'output.csv')
        """
    with open(fname, "w") as outfile:
        for i in al:
            outfile.write(str(i))
            outfile.write("\n")

def rprimes(fname):
    """This reads and returns a string containing a prime number list 

       Args:
           fname (str): Incorporates file name.
       Returns:
           plist: Generates integer list.
       Example:
           >>> list = rprimes('output.csv')
       """
    plist = []
    with open(fname) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            plist.append(row)
    return plist
