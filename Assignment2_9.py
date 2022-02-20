# 9. Write a program which accept number from user and return number of digits in that number.

def CountNumber(Number):
    iCnt = 0 
    iDigit = 0

    while(Number != 0):
        iCnt = iCnt+1
        Number = Number // 10

    return iCnt

def main():
    iNumber = int(input('enter the number :' ))
    iret = CountNumber(iNumber)
    print("Count of Digits in {0} Number is {1}".format(iNumber,iret))

if __name__=="__main__":
    main()