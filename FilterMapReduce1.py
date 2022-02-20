""" Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less
than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers """

from functools import reduce

""" def Product(Value):
    Meta = []
    for i in range(len(Value)):
        if(Value[i] >= 70 and Value[i] <= 90):
            Meta.append(Value[i])
    return Meta
 """
FilterX =  lambda Value1 :((Value1 >= 70) and (Value1 <= 90))


""" def MapX(ValueX):
    data = []
    for i in range(len(ValueX)):
        ddt = ValueX[i] + 10
        data.append(ddt)
    return data
  """
MapX = lambda iNo : iNo + 10


""" def Product3(Value3):
    Mult = 1
    for i in range(len(Value3)):
        Mult *= Value3[i]
    return Mult
 """
Rdx = lambda iVal, no : iVal * no

def main():
    Data = []
    iNum = int(input('How many number u want to store : '))

    for i in range(iNum):
        print("Enter input number ", i+1 ,end=" ->  ")
        Data.append(int(input()))

    iret1 = list(filter(FilterX,Data))
    print('List After Filtered : ',iret1)

    iret2 = list(map(MapX,iret1))
    print("List After Mapped : ",iret2)

    iRet3 = reduce(Rdx,iret2)
    print("Output After Reduce : ",iRet3)

if __name__=="__main__":
    main()


#  its also Valid 
"""from functools import reduce
    Data = []
    iNum = int(input('How many number u want to store : '))
    for i in range(iNum):
        Data.append(int(input()))
    print("Product of all Numbers is : ",reduce(lambda iVal, no : iVal * no, list(map( lambda iNo : iNo + 10, list(filter(lambda Value1 :((Value1 >= 70) and (Value1 <= 90)),Data))))))"""