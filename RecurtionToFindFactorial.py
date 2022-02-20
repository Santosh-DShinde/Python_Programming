""" 5. Write a recursive program which accept number from user and return its factorial.
Input : 5
Output : 120 """
# 1*2*3*4*5 = 120

i = 1
iMult = 1


def Factorial(no):
    global i, iMult
    if no >= 1:
        iMult *= i
        i += 1
        no -= 1
        Factorial(no)
    return iMult


def main():
    iNo = int(input('Enter the Number :'))
    print('Factorial Of {0} is {1} : '.format(iNo, Factorial(iNo)))


if __name__ == "__main__":
    main()
