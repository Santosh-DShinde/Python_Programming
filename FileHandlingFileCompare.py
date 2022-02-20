''' Write a program which accept two file names from user and compare contents of both the files. If both the files contains same
contents then display success otherwise display failure. Accept names of both the files from command line.  '''
from sys import*
import filecmp
import pathlib


def main():
    if len(argv) == 3:
        File = pathlib.Path(argv[1])
        if File.exists():
            Result = filecmp.cmp(argv[1], argv[2])
            if Result:
                print('Successful')
            else:
                print("Unsuccessful")
        else:
            print('Error : file Does not exists')
    else:
        print('''Error : Command line argument error
Enter valid argument''')


if __name__ == "__main__":
    main()