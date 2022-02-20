# 8. Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def DisplayPattern(iNo):
    for iCnt in range(1,iNo+1,1):
        for jCnt in range(1,iNo+1,1):
            if(iCnt >= jCnt):
                print(jCnt,end="  ")
        print()

def main():
    iNumber = int(input("Enter the number :"))
    DisplayPattern(iNumber)

if __name__=="__main__":
    main()