# 3. Write a program which accept one number from user and return its factorial.

def Factorial(Value):
    Fact = 1 

    for i in range(1,Value+1):
        Fact = Fact * i
        i = i + 1

    return Fact

def main():

    iRet = 0

    iNum = int(input("Enter The Number : "))
    iRet = Factorial(iNum)
    
    print("Factorial of {0} is {1} ".format(iNum,iRet))

if __name__=="__main__":
    main()


# Fact = 1
# iNo = int(input('Enter The Number : '))
# for i in range(1,iNo+1):
#     Fact = Fact * i
#     i = i+1
# print("Factorial of given Number is :",Fact)