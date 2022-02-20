""" .Write a program which contains one lambda function which accepts two parameters and return its multiplication. 
Input : 4 3 Output : 12 
Input : 6 3 Output : 18 """

iMult = lambda Value1, Value2: Value1 * Value2


def main():
    iNo1 = int(input('ENTER THE FIRST NUMBER : '))
    iNo2 = int(input('ENTER THE SECOND NUMBER : '))

    ret = iMult(Value2=iNo2, Value1=iNo1)
    print('Multiplication is {0} * {1} = {2}'.format(iNo1, iNo2, ret))


if __name__ == "__main__":
    main()
