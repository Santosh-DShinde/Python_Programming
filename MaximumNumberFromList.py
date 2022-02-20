""" Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List. """


def MaxReturn(MaxNum):
    Max = 0
    for i in range(len(MaxNum)):
        if Max <= MaxNum[i]:
            Max = MaxNum[i]
            
    return Max


def main():
    Data = []
    iNum = int(input("How many number you want to store : "))
    
    for i in range(iNum):
        Data.append(int(input()))
    iRet = MaxReturn(Data)
    
    print("maximum number from list is : ",iRet)


if __name__ == "__main__":
    main()
