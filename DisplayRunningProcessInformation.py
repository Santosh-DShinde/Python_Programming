"""Design automation script which accept process name and display information of that process if it is running."""
import psutil
from sys import*


def Process_Monitoring(Proc_Name=argv[1]):
    list_process = []

    for proc in psutil.process_iter():
        try:
            if Proc_Name.lower() in proc.name().lower():
                proc_info = ("Process_name", proc.name(), "PID",proc.pid, "Username",proc.username())
                list_process.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return list_process


def main():
    print("-----Marvellous : Automation & Machine Learning------")
    print(f"""Process monitoring.....🔍
\tProcess Name is - {argv[1]}
Information About {argv[1]} is as follow\n""")

    if len(argv) >2 or len(argv) < 2 :
        print('Error : Argumental error')

    if len(argv) == 2:
        try:
            lst_Process = Process_Monitoring()

        except Exception:
            print("Error : Invalid Args")

        for Process in lst_Process:
            print(Process)


if __name__ == "__main__":
    main()
