"""Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd
thread will display first 10 odd numbers. """

import threading

def Display_Even(No):
    iCnt = 0;i=0
    while iCnt != No:
        if i % 2 == 0:
            print('Even : ',i)
            iCnt+=1
        i+=1

def Display_Odd(No):
    iCnt=0;i=0
    while iCnt!=No:
        if i%2!=0:
            print('Odd : ',i)
            iCnt+=1
        i+=1

def main():
    No = int(input('Enter How Many Number U Want To Print : '))
    Thread1 = threading.Thread(target=Display_Even,args=(No,),name='Even_Thread')
    Thread2 = threading.Thread(target=Display_Odd,args=(No,),name='Odd_Thread')
    
    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__=="__main__":
    main()