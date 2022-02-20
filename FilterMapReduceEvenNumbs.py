""" Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
Map function will calculate its square. Reduce will return addition of all that numbers. """

from functools import reduce

FilterX = lambda Value1: (Value1 % 2 == 0)
MapX = lambda iNo: iNo * iNo
ReduceX = lambda no1, no2: no1 + no2


def main():
    data = []
    iNumber = int(input('enter how many number you want to store : '))
    for i in range(iNumber):
        data.append(int(input()))

    iRet1 = list(filter(FilterX, data))
    iRet2 = list(map(MapX, iRet1))
    iRet3 = reduce(ReduceX, iRet2)

    print("List after filter : {0} \nList after Map :{1} \nOutput of reduce :{2}".format(iRet1, iRet2, iRet3))


if __name__ == "__main__":
    main()
