# 4.Write a program which accept one number form user and return addition of its factors.

def FactAddition(Value):
    isum = 0

    for i in range(1,Value):
        if((Value % i)==0):
            isum = isum + i
        i = i + 1
    return isum

def main():
    ino = int(input('Enter The Number : '))

    iret = FactAddition(ino)
    print("Addition of {0}s Factors is {1}".format(ino, iret))

if __name__=="__main__":
    main()