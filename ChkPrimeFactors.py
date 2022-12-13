""" Write a program which contains one class named as Arithmetic.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),Factors().  
ChkPrime() method will returns true if number is prime otherwise return false.
    ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects. """


class Arithmetic:
    def __init__(self, a):
        self.Value = a

    def ChkPrime(self):
        flag = False
        for i in range(2, self.Value, 1):
            if self.Value % 2 == 0:
                break
            else:
                flag = True

    def ChkPerfect(self):
        Perft = self.SumFactors()

        if Perft == self.Value:
            return True
        else:
            return False

    def Factors(self):
        Fact = []
        print('Factors of Given Number Is As Below \n')
        for i in range(1, (self.Value // 2) + 1, 1):
            if self.Value % i == 0:
                Fact.append(i)
        print(Fact)
        return Fact

    def SumFactors(self):
        iSum = 0
        Fact = self.Factors()
        for i in range(len(Fact)):
            iSum += Fact[i]
        return iSum


def main():
    Ret = False
    iNo = int(input('Enter The Number : '))
    obj = Arithmetic(iNo)

    Ret = obj.ChkPrime()
    if Ret == True:
        print('Number is Prime')
    else:
        print('Number Is Not Prime')

    obj.Factors()

    Ret = False
    Ret = obj.ChkPerfect()
    if Ret == True:
        print('Number is Perfect')
    else:
        print('Number Is Not Perfect')

    print('Summation Of All Factors Is ', obj.SumFactors())


if __name__ == "__main__":
    main()
