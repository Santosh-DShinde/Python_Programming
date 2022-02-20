"""Write a program which contains one class named as Demo. Demo class contains two instance variables as no1 ,no2.
That class contains one class variable as Value.There are two instance methods of class as Fun and Gun which displays values of instance variables.
Initialise instance variable in init method by accepting the values from user. After creating the class create the two objects of Demo class as
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun() """


class Demo:
    Value = 30  # class variable

    def __init__(self, a, b):
        self.no1 = a  # instance variable
        self.no2 = b  # instance variable

    def Fun(self):  # instance Method
        print('inside Demo Fun ')
        print('value of no1 is {0} and value of no2 is {1} from Fun function'.format(self.no1, self.no2))
        print('Value of Class variable is : ', self.Value)

    def Gun(self):  # instance Method
        print('inside Demo Gun ')
        print('value of no1 is {0} and value of no2 is {1} From Gun function'.format(self.no1, self.no2))
        print('Value of Class variable is : ', self.Value)


def main():
    iNo1 = int(input('Enter The First Number'))
    iNo2 = int(input('Enter The Second Number'))

    Obj1 = Demo(iNo1, iNo2)
    Obj2 = Demo(iNo1, iNo2)

    Obj1.Fun()
    Obj1.Fun()
    Obj2.Gun()
    Obj2.Gun()


if __name__ == "__main__":
    main()
