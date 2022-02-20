""" Design automation script which accept directory name and display checksum of all files."""
from sys import *
import os
import hashlib


def Heading():
    Title = "="*90
    fd = open("LogFile.txt", "a")
    fd.write(Title)
    fd.write("\nchecksum Records of files \n")
    fd.write(Title)
    fd.write("\n")


def CheckSum(Dir_Name):
    if os.path.exists or os.path.isdir(Dir_Name):
        abs_Path = os.path.join(os.getcwd(), Dir_Name)
        if os.path.isabs(abs_Path):
            for file in os.listdir(abs_Path):
                file_name = file
                file = os.path.join(abs_Path, file)
                md5_hash = hashlib.md5( open(file, "rb").read()).hexdigest()
                fd = open("LogFile.txt", "a")
                data = f"\n CheckSum of {file_name} is {md5_hash} \n"
                fd.write(data)
                print(f"Checksum of file {file_name} is : ", md5_hash)
        else:
            print("Error : Path is not absolute path")
    else:
        print("Error : Path Does Not Exists")


def main():
    print("--------------- Marvellous : Automation Script------------------")
    print("Application Name is : ", argv[0])

    if len(argv) != 2:
        print("""Error : Invalid number of arguments
    For help  : -h or -H
    For Usage : -u or -U""")
        exit()

    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""This script accept one arguments as
argument is name of the directory
Expected Syntax -> Python Application_Name.py Directory_Name""")
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print("""Usage : This automation script is use to Find out Checksum of files""")
            exit()
        if os.path.exists(argv[1]):
            try:
                Heading()
                CheckSum(argv[1])
            except Exception as obj:
                print("Error : Invalid arguments")
        else:
            print("Error :path does not exists")


if __name__ == "__main__":
    main()
