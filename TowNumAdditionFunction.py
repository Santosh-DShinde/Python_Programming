# 3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Addition(iNo1 , iNo2):
  # return iNo1 + iNo2
    ans = 0
    ans = iNo1 + iNo2
    return ans
    
def main():
    ret = 0
    iNumber1 = int(input("Enter the First Number"))
    iNumber2 = int(input("Enter the Second Number"))

    ret = Addition(iNumber1,iNumber2)

    print("Addition is ",ret)

if __name__=="__main__":
    main()