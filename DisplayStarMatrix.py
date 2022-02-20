# 2. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def DisplayPattern(Value1):
    for i in range(Value1):
        for j in range(Value1):
            print('*',end="  ")
        print("\n")
               
def main():

    iNumber1 = int(input('Enter The Number : '))

    DisplayPattern(iNumber1)

if __name__=="__main__":
    main()