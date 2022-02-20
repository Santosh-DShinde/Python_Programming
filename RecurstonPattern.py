""" Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5 
"""

def DisplayNum(Number):
    LST = []
    i=0
    if Number>=i:  
        LST.append(Number)
        Number-=1
        DisplayNum(Number)
    
    LST.reverse()
    print(LST,end="  ")    

def main():
    iNo = int(input('Enter the number : '))
    DisplayNum(iNo)
    
if __name__=="__main__":
    main()