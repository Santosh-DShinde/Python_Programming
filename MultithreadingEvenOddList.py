"""Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter.
Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and
display the addition"""

import threading

iSum = 0;
OSum = 0
i = 0


def Evenlist(data1):
    EvenLst = [];
    global iSum
    for i in data1:
        if i % 2 == 0:
            EvenLst.append(i)
            iSum += i
    print("Even Number List is : ", EvenLst)
    print("Summation Of All Even Numbers Is : ", iSum)


def OddList(data2):
    OddLst = [];
    global OSum
    for i in data2:
        if i % 2 != 0:
            OddLst.append(i)
            OSum += i
    print("Odd Number List is : ", OddLst)
    print("Summation Of All Odd Numbers Is : ", OSum)


def main():
    ActualList = [11, 45, 24, 74, 14, 44, 51, 10, 40, 51, ]

    evenlist = threading.Thread(target=Evenlist, args=(ActualList,), name='evenlist')
    oddlist = threading.Thread(target=OddList, args=(ActualList,), name='oddlist')

    evenlist.start()
    oddlist.start()


if __name__ == "__main__":
    main()
