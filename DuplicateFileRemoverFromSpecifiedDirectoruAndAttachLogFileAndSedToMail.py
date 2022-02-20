"""Design automation script which performs following task.-----
1)  ✔ Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
2)  ✔ Create one Directory and inside that directory create log file which maintains all names of duplicate files which are deleted.
3)  ✔ Name of that log file should contains the date and time at which that file gets created.
4)  ✔ Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
5)  ✔ Accept Mail id from user and send the attachment of the log file.
Mail body should contains below things :---------------
6)  ✔ Starting time of scanning
7)  ✔ Total number of files scanned
8)  ✔ Total number of duplicate files found
       Note :-------
9)  ✔ For every separate task write separate function.
10) ✔ Write all user defined functions in one user defined module.
11) ✔ Use proper validation techniques.
12) ✔ Provide Help and usage option for script.
13) ✔ Mail body should contains statistics about the operation of duplicate file removal.
"""
import hashlib
import math
import os
import schedule
import smtplib
import time
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from sys import *
from urllib.request import urlopen


def is_connected():
    try:
        urlopen("https://www.google.co.in/", timeout=1)
        return True
    except Exception as obj:
        return False


def Create_Files(Name, DirName='LogFiles'):
    global abs, fd
    File_Name = DirName + datetime.now().strftime("%H-%M-%S") + ".txt"
    if not os.path.exists(DirName):
        os.mkdir(DirName)
    for root, dir, file in os.walk("."):
        for dirnames in dir:
            abs = os.path.join(os.getcwd(), DirName, File_Name)
            if not os.path.exists(abs):
                fd = open(abs, "a")
                fd.write("=" * 80)
                fd.write(f"\nRecords of Removed Duplicate Files From Directory : {Name} \n")
                fd.write("=" * 80)
                fd.write("\n")

    RemoveDuplicateFiles(Name, fd, abs, File_Name)


def RemoveDuplicateFiles(Dups, fd, fileName, LogFileName):
    StartTime = time.time()
    Unique = {}
    icnt = 0; ncounter = 0
    try:
        if os.path.exists(Dups):
            for root, directory, file in os.walk(Dups):
                for files in file:
                    icnt += 1
                    file = os.path.join(os.getcwd(), Dups, files)
                    if not os.path.isdir(file) and os.path.isfile(file):
                        HashCode = hashlib.md5(open(file, "rb").read()).hexdigest()
                        if HashCode not in Unique:
                            Unique[HashCode] = file
                        else:
                            ncounter += 1
                            os.remove(file)
                            # print(f"Successfully deleted {file}")
                            fd.write(f"\n{file} File gets successfully deleted\n")
            if ncounter == 0:
                fd.write(f"No Duplicate Files Found in {Dups} Directory \n")
            else:
                fd.write(f"\n{ncounter} Duplicate files found ")

        fd.close()

    except Exception as obj:
        print("Exception Occurred : ", obj)

    ExeTime = (time.time() - StartTime)
    ExeTime = round(ExeTime, 4)
    mail_Sending(File_Name=fileName, Counter=icnt, NumberOfFileFound=ncounter, Executiontime=ExeTime,
                 LogFileName=LogFileName)


def mail_Sending(File_Name, Counter, NumberOfFileFound, Executiontime, LogFileName):
    try:
        Sender = "shindesan3047@gmail.com"
        Receiver = argv[3]
        password = "YourPassword"

        msg = MIMEMultipart()
        msg['From'] = Sender
        msg['To'] = Receiver
        Subject = """
        Process log generated at : %s """ % (datetime.now().strftime("%H_%M_%S"))
        msg['Subject'] = Subject
        body = """
        Hello %s,  
        Total %d files scanned
        Total %d duplicate file found
        Time required for this script is %s
        Please find attached document which contains records of removed duplicates files at : %s 

        This is auto generated mail.
                           \n\n\n\n\n\n\n 
                                      Thanks & Regards,
                                      Santosh  Shinde
            """ % (Receiver, Counter, NumberOfFileFound, Executiontime, datetime.now().strftime("%H_%M_%S"))

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(File_Name, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload(attachment.read())
        encoders.encode_base64(p)

        p.add_header('content-Disposition', 'attachment;  filename= "%s" ' % LogFileName)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(Sender, password)

        text = msg.as_string()

        s.sendmail(Sender, Receiver, text)

        s.quit()

        # print("Log File sent through mail")

    except Exception as obj:
        print("Exception Occurred mail send: ", obj)


def main():
    print(f"""\n-----------: Wellcome To World Of Programming :--------------\n
application name is : {argv[0].split(".")[0]}""")

    if len(argv) < 2 or len(argv) > 4 or len(argv) == 3:
        print('''Error : Argumental error, please refer below flags for help or usage 
For help  : -h or -H
For Usage : -u or -U''')
        exit()

    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""Help : We are happy to help you, please follow below instructions for proper execution of the Application
This Application accepts three commandline arguments as -
<1>first argument is absolute path of directory which may contains duplicate files
<2>second argument is time interval of script in minutes
<3>third argument is <mail id> of receive
Note : This application works only when internet connection is available on your  machine otherwise application collapse  
expected syntax : <"Application_Name.py  Dir_Name_WhichMayContainsDuplicateFiles  TimeForScheduleScriptInMinutes  Receiver_MailID">
""")
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print("""Usage : The use of this application is to <"Remove the duplicate files from specific Directory or specified path">
and create LogFile into new directory which create while running script this directory contains the all records about deleted duplicate files.
after writing record into file send that LogFile to anybody who do you want to send through mail which is accepted from user """)
            exit()

    if len(argv) == 4:
        if is_connected():
            print(f"""please wait while Processing.....🔍
wait for {argv[2]} minutes""")
            try:
                schedule.every(int(argv[2])).minutes.do(Create_Files, argv[1])
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except Exception as obj:
                print("Exception Occurred : ", obj)
        else:
            print("Oops : You're offline. Check your internet connection")
            exit()


if __name__ == "__main__":
    main()
