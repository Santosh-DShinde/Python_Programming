# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise
# return false.

def ChkDivisible(Num):
    if((Num % 5)==0):
        return True
    else:
        return False

def main():
    bRet = False
    iNumber = int(input("Enter The Number"))

    bRet = ChkDivisible(iNumber)

    if(bRet == True):
        print("True")
    else:
        print("False")

if __name__=="__main__":
    main()