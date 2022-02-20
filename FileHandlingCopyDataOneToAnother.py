"""Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from
 existing file into new file. Accept file name through command line arguments."""

import os
from sys import*


def main():
    if len(argv) == 3:
        fd = open(argv[1], "r")
        sd = open(argv[2], "w")
        for data in fd:
            sd.write(data)
        print(f'data successfully copied from {argv[1]} to {argv[2]}')
    else:
        print('''Error : argument error
Please enter two file names from which you have to copy data into in which you have to write ''')


if __name__ == "__main__":
    main()
