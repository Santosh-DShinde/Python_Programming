""" Write a program which contains one lambda function which accepts one parameter and return power of two. """

from functools import reduce

# def Power(iNo):
#     iPower = 1
#     for i in range(iNo):
#         iPower *= 2
#     return iPower

Power = lambda no: no ** 2


def main():
    iNumber = int(input('Enter the Value : '))

    iret = (Power, iNumber)
    print('Power of {0} is {1}'.format(iNumber, iret))


if __name__ == "__main__":
    main()
