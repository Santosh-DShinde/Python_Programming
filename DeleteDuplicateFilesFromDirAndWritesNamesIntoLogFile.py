"""Design automation script which accept directory name and delete all duplicate files from that directory. Write names
of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory."""

from sys import *
import os
from pathlib import Path
import hashlib


def Heading():
    Title = "=" * 90
    fd = open("LogFile.txt", "a")
    fd.write(Title)
    fd.write("\nRecord of duplicate files removed\n")
    fd.write(Title)
    fd.write("\n")


def Duplicate_file_Detector(Dir_Name):
    Unique = {}
    if os.path.exists or os.path.isdir(Dir_Name):
        Abs_Path = os.path.join(os.getcwd(), Dir_Name)
        for files in os.listdir(Abs_Path):
            File = files
            File_Name = os.path.join(Abs_Path, files)
            file_Hash = hashlib.md5(open(File_Name, "rb").read()).hexdigest()
            if file_Hash not in Unique:
                Unique[file_Hash] = File_Name
            else:
                os.remove(File_Name)
                print(f"Duplicate file Deleted - {File} ")
                fd = open("LogFile.txt", "a")
                data = f"\nDuplicate file deleted - {File}\n"
                fd.write(data)


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
            print("""Usage : This automation script is use to Find out Duplicate files from specified directory
and writes their names in log file""")
            exit()

        if os.path.exists(argv[1]):
            try:
                Heading()
                Duplicate_file_Detector(argv[1])

            except Exception as obj:
                print("Error : Invalid arguments")
        else:
            print("Error :path does not exists")


if __name__ == "__main__":
    main()
