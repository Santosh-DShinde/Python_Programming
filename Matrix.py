# 7. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def Display(iValue):
    for i in range(1,iValue+1,1):
        for j in range(1,iValue+1,1):
            print(j,end="  ")
        print()

def main():
    iNum = int(input('Enter The Number : '))
    Display(iNum)

if __name__=="__main__":
    main()


#          Snippest Code
# ino = int(input("Enter the number : "))
# for i in range(1,ino+1,1):
#     for j in range(1,ino+1,1):
#          print(j,end="  ")
#     print()