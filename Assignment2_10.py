# 10. Write a program which accept number from user and return addition of digits in that number.
def SumDigits(iNo):
    iSum = 0; iDigit = 0 
    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10    
    
    return iSum


def main():
    value = int(input('enter the number :' ))
    iRet = SumDigits(value)
    print("Addition of Digits of {0} number is {1}".format(value,iRet))

if __name__=="__main__":
    main()