# 1.Create one module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for
# multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program 
# which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    iNo1 = (int(input('Enter The First Number :  ')))
    iNo2 = (int(input('Enter The Second Number : ')))

    iRet1 = Arithmetic.Add(iNo1,iNo2)
    iRet2 = Arithmetic.Sub(iNo1,iNo2)
    iRet3 = Arithmetic.Mult(iNo1,iNo2)
    iRet4 = Arithmetic.Div(iNo1,iNo2)

    print('{0} + {1} = {2}'.format(iNo1, iNo2, iRet1))
    print('{0} - {1} = {2}'.format(iNo1, iNo2, iRet2))
    print('{0} * {1} = {2}'.format(iNo1, iNo2, iRet3))
    print('{0} / {1} = {2}'.format(iNo1, iNo2, iRet4))

if __name__=="__main__":
    main()