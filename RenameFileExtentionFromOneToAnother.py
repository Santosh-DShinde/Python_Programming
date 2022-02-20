"""Design automation script which accept directory name and two file extensions from user. Rename all files with first
file extension with the second file extension. """
import os.path
from sys import *


def Rename_File():
    if os.path.exists(os.path.join(os.getcwd(), argv[1])):
        for file in os.listdir(argv[1]):
            if file.endswith(argv[2]):
                oldExt = os.path.join(os.getcwd(), argv[1], file)
                os.rename(oldExt, oldExt.split(".")[0] + argv[3])
                print(f"{file} Renamed successfully")
    else:
        print("Error :Path does not exist")


def main():
    print("--------------- Marvellous : Automation Script------------------")
    print("Application Name is : ", argv[0].split(".")[0])
    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""This script accept three arguments as 
First  argument is name of the directory
second argument is old extension of file that you want change from
third  argument is new extension of file that you want to set 
Expected Syntax -> Python Application_Name.py Directory_Name Old_File_Extension New_File_Extension""")
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print("Usage : This automation script is use to change extension of file ")
            exit()

        else:
            print("Error : There is no such a flag")
            exit()

    if len(argv) == 4:

        try:
            Rename_File()

        except Exception:
            print("Error : Invalid arguments")

    if len(argv) < 2 or len(argv) > 4:
        print("""Error : Invalid number of arguments
For help  : -h or -H 
For Usage : -u or -U""")
        exit()


if __name__ == "__main__":
    main()
