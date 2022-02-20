# 6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def ChkPositive(iNo):
    if(iNo >= 1):
       return 1
        #print("Entered Number Is Positive")
    elif(iNo < 0):
       return 2
       # print("The Number is Negative")
    elif(iNo == 0):
       return 3
       # print("the Number is Zero")

def main():

    bRet = False
    iNumber = int(input("Enter The Number :"))
    bRet = ChkPositive(iNumber)    

    if(bRet == 1):
        print("Entered Number Is Positive")
    elif(bRet == 2):
        print("The Number is Negative")
    elif(bRet == 3):
        print("the Number is Zero")

if __name__=="__main__":
    main()

