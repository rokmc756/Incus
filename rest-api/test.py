#!/usr/bin/python3

import getopt
import sys
from math import sqrt

"""
get the square but get the square root in case the argument 'root' is provided
"""


def usage():
    """
    Show help for the CLI program
    """
    print("python advanced_square.py --number <your_number> \n OR\n")
    print("python advanced_square.py -n <your_number>\n")
    print("To get the square root: python advanced_square.py -n <your_number> -r")
    print("Example: get the square\n\tpython advanced_square.py -n 5")



def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hn:r",["help","number=","root"])
    except getopt.GetoptError as error:
        print(error)
        sys.exit()

    # initialize variables for for loop
    number = None
    root_number = False

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-n", "--number"):
            print(arg)
            number = int(arg)
        elif opt in ('-r','--root'):
            root_number = True
        else:
            usage()
            sys.exit()

    #if root_number:
    #    print(f"The square root of {number} = {sqrt(number)}")
    #else:
    #    print(f"The square of {number} = {number* number} ")


if __name__ == '__main__':
    main()


