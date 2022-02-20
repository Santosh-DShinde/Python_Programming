"""Write a program which accept number from user and print that number of " * " on screen."""


def Display(iNum):
    for i in range(0,iNum,1):
        print(" * ", end="")


def main():
    iNo = int(input("Enter The Number"))
    Display(iNo)


if __name__ == "__main__":
    main()
