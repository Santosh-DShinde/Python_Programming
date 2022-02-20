# 5.Write a program which accept one number for user and check whether number is prime or not.

def ChkPrime(Value):
    flag = False

    for i in range(2,Value,1):
        if((Value % i) == 0):
            flag = True
   
    return flag            

def main():
    iNo = int(input("Enter The Number : " ))
    bret = ChkPrime(iNo)
    if(bret == True):
        print("Is Is Not Prime Number")
    else:
        print("It is prime number")

if __name__=="__main__":
    main()