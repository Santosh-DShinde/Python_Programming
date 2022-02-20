"""Write a program which accepts file name from user and check whether that file exists in current directory or not."""
from os.path import exists


def main():

    name = input('Enter  File Name : ')
    if exists(name):
        print('File is Exist...')
    else:
        print('Error : File Does Not Exist...')


if __name__=="__main__":
    main()