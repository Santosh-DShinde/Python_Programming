""" ✔ Design automation script which accept directory name and file extension from user. Display all files with that
extension. """
import os.path
from sys import *


def DisplayFiles(Dir_Name, File_Extension):
    try:
        if os.path.exists(os.path.join(os.getcwd(), Dir_Name)):
            for file in os.listdir(Dir_Name):
                if file.endswith(File_Extension):
                    print(file)
        else:
            print("Error : Path does not exists")
    except Exception as obj:
        print("""Exception Occurred : """, obj)


def main():
    print("--------------- Marvellous Automation Script------------------")
    print("Application Name is : ", argv[0].split(".")[0])
    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""This script accept two arguments as 
First argument is name of the directory
and second argument is extension of file that you want to display
Expected Syntax -> Python Application_Name.py Directory_Name File_Extension""")
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print(
                "Usage : This automation script is use to display desire extension files from directory if it is exist")
            exit()

        else:
            print("There is no such flag...")
            exit()

    if len(argv) == 3:
        try:
            DisplayFiles(Dir_Name=argv[1], File_Extension=argv[2])

        except Exception:
            print("Error : Invalid arguments")

    if len(argv) < 2 or len(argv) > 3:
        print("""Error : Invalid number of arguments
For help  : -h or -H 
For Usage : -u or -U""")
        exit()


if __name__ == "__main__":
    main()
