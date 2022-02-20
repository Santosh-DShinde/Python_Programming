"""Write a program which contains one class named as Circle. Circle class contains three instance variables as Radius ,Area, Circumference .
That class contains one class variable as PI which is initialised to 3.14.
Inside init method initialise all instance variables to 0.0.  
There are three instance methods inside class as Accept() , Calculate Area(),CalculateCircumference(), Display().
Accept method will accept value of Radius from user.///
CalculateArea() method will calculate area of circle and store it into instance variable Area.     #
CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
And Display() method will display value of all the instance variables as Radius , Area, Circumference.
After designing the above class call all instance methods by creating multiple objects. """


# formulas
# A = PI r^2
# C = 2 \pi r
class Circle:
    PI = 3.14

    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.Radios = a
        self.Area = b
        self.Circumference = c

    def Accept(self):
        iNo = int(input('Enter the radios : '))
        self.Radios = iNo

    def Calculate_Area(self):
        self.Area = self.PI * self.Radios * self.Radios

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radios

    def Display(self):
        print('Area of circle is is : ', self.Area)
        print('Circumference of circle is : ', self.Circumference)


def main():
    obj = Circle()
    obj.Accept()
    obj.Calculate_Area()
    obj.CalculateCircumference()
    obj.Display()


if __name__ == "__main__":
    main()
