""" 1. Write a recursive program which display below pattern.
Input : 5
Output : * * * * *               """


def Display(Num):
    if Num >= 1:
        print('*', end="  ")
        Num -= 1
        Display(Num)


def main():
    iNo = int(input('Enter The Number : '))
    Display(Num=iNo)


if __name__ == "__main__":
    main()
