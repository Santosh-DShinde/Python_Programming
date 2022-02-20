"""Write a program which contains one class named as Arithmetic. Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0. There are three instance methods inside class as Accept(), Addition(),
Subtraction(),Multiplication(), Division(). Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects. """


class Arithmetic:
    def __init__(self, no1=0, no2=0, no3=0):
        self.Value1 = no1
        self.Value2 = no2
        self.Value3 = no3

    def Accept(self):
        iNo1 = int(input('Enter the First Number : '))
        iNo2 = int(input('Enter the Second Number : '))
        self.Value1 = iNo1
        self.Value2 = iNo2

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        Div = 0.0
        try:
            Div = self.Value1 / self.Value2
        except ZeroDivisionError as obj:
            print('Exception Occurred Which is -> ', obj)
        finally:
            pass
        return Div


def main():
    obj = Arithmetic()
    obj.Accept()
    print("Addition is : ", obj.Addition())
    print("Subtraction is : ", obj.Subtraction())
    print("Multiplication is : ", obj.Multiplication())
    print('Divisions is : ', obj.Division())


if __name__ == "__main__":
    main()
