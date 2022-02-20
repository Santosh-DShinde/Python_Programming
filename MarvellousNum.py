def ChkPrime(Value):
    Lst = [] ; iSum = 0
    for i in range(len(Value)):
        flag = True
        for j in range(2,Value[i]):
            if(Value[i] % j == 0):
                flag = False
                break
        if(flag == True):
            Lst.append(Value[i])
            iSum += Value[i]
    return iSum
