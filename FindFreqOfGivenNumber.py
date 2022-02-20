""" Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List. """


def CountFreq(Value, iNo):
    iCnt = 0
    for i in range(len(Value)):
        if Value[i] == iNo:
            iCnt = iCnt + 1

    return iCnt


def main():
    Data = []
    iNum1 = int(input("How many number you want to store : "))
    iNum2 = int(input('Enter the number : '))

    for i in range(iNum1):
        Data.append(int(input()))
    iRet = CountFreq(Data, iNum2)

    print("Frequency of {0} is {1}: ".format(iNum2, iRet))


if __name__ == "__main__":
    main()
