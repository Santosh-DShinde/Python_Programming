"""Design automation script which accept two directory names and one file extension. Copy all files with the specified
extension from first directory into second directory. Second directory should be created at run time."""
import os
import os.path
import time
from sys import*
import shutil
import schedule


def Heading():
    Title = "="*100
    fd = open("LogFile.txt", "a")
    fd.write(Title)
    fd.write("\nCopied Files With Extensions Records\n")
    fd.write(Title)


def Copy_Dir(Src, Des, Ext):
    if not os.path.exists(Des):
        os.mkdir(Des)
    if os.path.exists(Des):
        files = os.listdir(Src)
        for file in files:
            if file.endswith(Ext):
                shutil.copy2(os.path.join(Src, file), Des)
                fd = open("LogFile.txt", "a")
                data = f"\n{file} File copied from {Src} Directory to {Des} Directory successfully\n"
                fd.write(data)
                print(f"{file} File copied from {Src} Directory to {Des} Directory successfully")
    else:
        print("Error : Enable to create directory or directory does not exists")


def main():
    print("--------------- Marvellous : Automation Script------------------")
    print("Application Name is : ", argv[0])
    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""This script accept three arguments as 
First  argument is name of the Src_directory_Name
second argument is Name of the Des_Directory_Name
third  argument is extension of file 
Expected Syntax -> Python Application_Name.py Src_Directory_Name Des_Dir_Name File_Extension""")
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print("""Usage : This automation script is use to copy the specified extension files into specified 
            Des.tination directory""")
            exit()

        else:
            print("Error : There is no such a flag")
            exit()

    if len(argv) == 4:

        try:
            Heading()
            schedule.every(1).minutes.do(Copy_Dir, argv[1], argv[2], argv[3])
            while True:
                schedule.run_pending()
                time.sleep()

        except Exception as obj:
            print("Error : Invalid arguments")

    if len(argv) < 2 or len(argv) > 4 or len(argv) == 3:
        print("""Error : Invalid number of arguments
For help  : -h or -H 
For Usage : -u or -U""")
        exit()


if __name__ == "__main__":
    main()
