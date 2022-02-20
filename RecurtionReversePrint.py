"""Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1 """


def DisplayRevNum(Number):
    i = 0
    if Number > i:
        print(Number, end="  ")
        Number -= 1
        DisplayRevNum(Number)


def main():
    iNo = int(input('Enter the number : '))
    DisplayRevNum(iNo)


if __name__ == "__main__":
    main()
