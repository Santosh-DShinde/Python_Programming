"""Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter.
Small thread display number of small characters, capital thread display number of capital characters and digits thread display number
 of digits. Display id and name of each thread. """

import threading


def SmallX(String_of_Small):
    print('Thread id of Small thread is {0} and thread name is {1}'.format(threading.currentThread().ident,
                                                                           threading.current_thread()))
    # SmallLst = []
    iCnt = 0
    for i in String_of_Small:
        if i.islower():
            iCnt += 1
            print(i, end=" ")
    print('\nNumber of Small characters is : ', iCnt)
    # SmallLst.append(i)
    # print(SmallLst)             


def CapitalX(String_of_Capital):
    print('Thread id of Capital thread is {0} and thread name is {1}'.format(threading.currentThread().ident,
                                                                             threading.current_thread()))
    iCnt = 0
    for i in String_of_Capital:
        if i.isupper():
            iCnt += 1
            print(i, end=" ")
    print('\nNumber of Capital characters is : ', iCnt)


def DigitX(String_of_Digit):
    print('Thread id of Digit thread is {0} and thread name is {1}'.format(threading.currentThread().ident,
                                                                           threading.current_thread()))
    iCnt = 0
    for i in String_of_Digit:
        if i.isdigit():
            iCnt += 1
            print(i, end=" ")
    print('\nNumber of Digits is : ', iCnt)


def main():
    StringX = 'ThorTheGodOfThunder1234@Gmail.Com'

    Small = threading.Thread(target=SmallX, args=(StringX,), name='SmallThread')
    Capital = threading.Thread(target=CapitalX, args=(StringX,), name='CapitalThread')
    Digit = threading.Thread(target=DigitX, args=(StringX,), name='DigitThread')

    Small.start()
    Capital.start()
    Digit.start()

    Small.join()
    Capital.join()
    Digit.join()

    print('\nEnd Execution')


if __name__ == "__main__":
    main()
