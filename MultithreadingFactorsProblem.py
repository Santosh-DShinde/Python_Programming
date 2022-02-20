"""Design python application which creates two threads as evenfactor and oddfactor. Both the thread accept one parameter as integer.
Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number.
After execution of both the thread gets completed mainthread should display message as "exit from main. """

import threading


def Add_Of_Even_Fact(iNo):
    iSum = 0
    for i in range(1, iNo):
        if iNo % i == 0:
            if i % 2 == 0:
                iSum += i

    print('Summation Of All Even Factors is : {0}'.format(iSum))


def Add_Of_Odd_Fact(iNo):
    Sum = 0
    for i in range(1, iNo):
        if iNo % i == 0:
            if i % 2 != 0:
                Sum += i
    print('Summation Of All  Odd Factors is : {0}'.format(Sum))


def main():
    iNum = int(input('Enter the number : '))

    evenfactor = threading.Thread(target=Add_Of_Even_Fact, args=(iNum,), name='EvenFactor')
    oddfactor = threading.Thread(target=Add_Of_Odd_Fact, args=(iNum,), name='oddFactor')

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("Exit From Main...")


if __name__ == "__main__":
    main()
