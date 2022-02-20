"""Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List. """


def Addition(Numbers):
    iSum = 0
    for i in range(len(Numbers)):
        iSum = iSum + Numbers[i]

    return iSum


def main():
    Data = []
    
    iNumber = int(input('How many Number you want to store ? : '))
    
    for i in range(1,iNumber+1,1):
        print('Enter Data Number',i," :-> ",end="  ")
        Data.append(int(input()))
    
    iRet = Addition(Data)
    print('Addition if all numbers is : ',iRet)


if __name__ == "__main__":
    main()
