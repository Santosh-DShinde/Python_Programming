# 6. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# * * * * *
# * * * *
# * * *
# * *
# *

def Display(Value):

    for i in range(1,Value+1,1):
        for j in range(1,Value+1,1):
            if(i <= j):
                print('*',end="  ")
        print()

def main():
    iNum = int(input('enter the number'))

    Display(iNum)

if __name__=="__main__":
    main()