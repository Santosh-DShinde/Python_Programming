""" Design python application which contains two threads named as thread1 and thread2. Thread1 display 1 to 50 on screen and thread2
 display 50 to 1 in reverse order on screen. After execution of thread1 gets completed then schedule thread2. """

import threading


def Forward_Print():
    for i in range(1, 50 + 1, 1):
        print(i)


def Backword_Print():
    for i in range(50, 1 - 1, -1):
        print(i)


def main():
    thread1 = threading.Thread(target=Forward_Print, name="thread1")
    thread2 = threading.Thread(target=Backword_Print, name="thread2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
