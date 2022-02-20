"""Design automation script which display information of running processes as its name, PID, Username."""
import time
import psutil
import schedule


def Display_Running_Process():
    list_process = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            list_process.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for processes in list_process:
        print(processes)


def main():
    print("-----Marvellous : Automation & Machine Learning------")
    print("Process monitoring")

    schedule.every(10).seconds.do(Display_Running_Process)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
