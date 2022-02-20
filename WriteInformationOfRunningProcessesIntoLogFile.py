"""Design automation script which accept directory name from user and create log file in that directory which contains
information of running processes as its name, PID, Username."""
import psutil
from sys import*


def Create_Logfile():
    fd = open("LogFile.txt", "a")
    Heading = "="*100
    fd.write(Heading)
    fd.write("\nRecords of Running Processes\n")
    fd.write(Heading)
    fd.write("\n")


def Process_Monitoring( ):
    list_process = []
    fd = open("LogFile.txt", "a")
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            list_process.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    Info = str(list_process)
    fd.write(Info)
    fd.write("\n")
    fd.close()


def main():
    print("-----Marvellous : Automation & Machine Learning------")

    if len(argv) >2 or len(argv) < 2 :
        print('Error : Argumental error')

    if len(argv) == 2:
        try:
            Create_Logfile()
            Process_Monitoring()

        except Exception:
            print("Error : Invalid Args")


if __name__ == "__main__":
    main()
