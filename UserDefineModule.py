"""Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from
that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of
our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime(). """

import MarvellousNum


def main():
    Data = []
    iNum = int(input("How many Number You Want to Store ? "))

    for i in range(1, iNum + 1, 1):
        print("Enter input number ", i, end=" -> ")
        Data.append(int(input()))

    iRet = MarvellousNum.ChkPrime(Data)
    print('Addition of all prime numbers is : ', iRet)


if __name__ == "__main__":
    main()
