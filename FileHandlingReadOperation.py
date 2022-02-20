"""Write a program which accept file name from user and open that file and display the contents of that file on 
screen."""

from os.path import exists


def main():
    File_NameX = input('Enter File Name : ')
    if exists(File_NameX):
        fd = open(File_NameX, 'r')

        data = fd.read()
        print('Data From the File Is : ', data)
    else:
        print('Error : File Does Not Exist...')


if __name__ == "__main__":
    main()
