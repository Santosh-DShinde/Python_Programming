""" Write a program which accept N numbers from user and store it into List. Return minimum
number from that List. """


def miniReturn(Value):
    for j in range((len(Value)) - 1, len(Value), 1):
        mini = Value[j]

    for i in range(len(Value)):
        if Value[i] <= mini:
            mini = Value[i]

    return mini


def main():
    Data = []
    iNum = int(input("How many number you want to store : "))

    for i in range(iNum):
        Data.append(int(input()))
    iRet = miniReturn(Data)

    print("miniimum number from list is : ", iRet)


if __name__ == "__main__":
    main()
