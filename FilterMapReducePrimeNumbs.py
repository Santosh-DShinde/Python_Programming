""" Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. 
(You can also use normal functions instead of lambda functions) """


def CheckPrime(Value):
    Lst = []

    for i in range(len(Value)):
        flag = True
        for j in range(2, Value[i]):
            if (Value[i] % j == 0):
                flag = False
                j += 1
                break
        if flag:
            Lst.append(Value[i])
    return Lst


MapX = lambda Value2: (Value2 * 2)


def ReduceX(Value3):
    iMax = 0
    for i in range(len(Value3)):
        if iMax < Value3[i]:
            iMax = Value3[i]
    return iMax


def main():
    Data = []
    iNum = int(input("Enter how many number you want to store : "))

    for i in range(1, (iNum) + 1):
        print("Enter input Number", i, " -> ", end="  ")
        Data.append(int(input()))

    iRet = CheckPrime(Data)
    print("Prime list is :-> ", iRet)

    iRet2 = list(map(MapX, iRet))
    print(" Data map is ", iRet2)
    iRet3 = ReduceX(iRet2)
    print("Max data is : ", iRet3)


if __name__ == "__main__":
    main()
