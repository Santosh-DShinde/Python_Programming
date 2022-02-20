"""Design automation script which accept two directory names. Copy all files from first directory into second directory.
Second directory should be created at run time."""
import time
from sys import *
import os
import shutil
import schedule


def Heading():
    Title = "="*100
    fd = open("LogFile.txt", "a")
    fd.write(Title)
    fd.write("\nCopied Files Records\n")
    fd.write(Title)


def Copy_Dir(Dest):
    if not os.path.exists(Dest):
        os.mkdir(Dest)
    if os.path.exists(Dest):
        files = os.listdir(argv[1])
        for file in files:
            shutil.copy2(os.path.join(argv[1], file), Dest)
            fd = open("LogFile.txt", "a")
            data = f"\n{file} File copied from {argv[1]} Directory to {Dest} Directory successfully\n"
            fd.write(data)
            print(f"{file} File copied from {argv[1]} Directory to {Dest} Directory successfully")
    else:
        print("Error : Enable to create directory or directory does not exists")


def main():
    print("-------------------  Marvellous : Automation script  ---------------------")
    print("Script Name : ", argv[0].split(".")[0])
    print("Number of arguments accepted : ", len(argv) - 1)

    if (len(argv) > 3) or (len(argv) < 2):
        print("Error : Invalid Number of Arguments")
        print("""For Help : use -h or -H
For Usage : use -u or -U""")
        exit()

    if len(argv) == 2:
        if argv[1] == "-u" or argv[1] == "-U":
            print("Usage : Script is used to copy all files from specified directory to given directory name")
            exit()

        elif (argv[1] == "-h") or (argv[1] == "-H"):
            print("""Help : We are happy to help you, please follow instructions for better execution.
First_Argument  : Directory name from where you you want to select all files
Second argument : New Directory name in which you want to paste the files
Expected syntax is : applicationName.py  SrcDirName  DestDirName""")
            exit()

        else:
            print("There is no such flag...")
            exit()

    if len(argv) == 3:
        try:
            print("Please Wait For Minute")
            Heading()
            schedule.every(1).minutes.do(Copy_Dir, argv[2])
            while True:
                schedule.run_pending()
                time.sleep(1)

        except Exception as obj:
            print("""Exception while executing the script : %s\n
Please check the input or contact the developer..""" % obj)
            exit()


if __name__ == "__main__":
    main()
