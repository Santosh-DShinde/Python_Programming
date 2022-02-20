""" 4.Write a recursive program which accept number from user and return summation of its digits.
Input : 879
Output : 24 """

Sum = 0


def SumDigits(No):
    global Sum
    if No != 0:
        Digit = No % 10
        Sum += Digit
        No //= 10
        SumDigits(No)
    return Sum


def main():
    iNo = int(input('enter the number : '))
    print("Summation Of Given Number Is : ", SumDigits(iNo))


if __name__ == "__main__":
    main()

# No = 123456
# Sum = 0 
# for Digit in str(No):
#      Sum+=int(Digit)
# print(Sum)
