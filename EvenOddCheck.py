# 2. Write a program which contains one function named as ChkNum() which accept one  parameter as number. If number is even then it 
# should display "Even number" otherwise display "Odd number" on console.


def ChkNum(Number):
    if((Number %2) == 0):
        print("Enven Number")
    else:
        print("Odd Number")

def main():
    
    iNumber = int(input("Enter the Number : "))
    
    ChkNum(iNumber)
    
if __name__=="__main__":
    main()