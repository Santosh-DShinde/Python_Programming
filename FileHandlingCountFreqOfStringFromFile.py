""" Accept file name and one string from user and return the frequency of that string from file."""
import os


def main():
    File_Name = input('Enter File Name : ')
    StringX = input('Enter String : ')
    fd = open(File_Name, "r")
    data = fd.read()
    print(f'Occurrence of {StringX} is {data.count(StringX)} in {File_Name} File')


if __name__ == "__main__":
    main()

    '''Count Function argument should be string, not int'''
