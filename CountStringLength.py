# 10. Write a program which accept name from user and display length of its name.

def DisplayStr(str):
    print(len(str))

def main():
    str =input ("Enter String ")
    DisplayStr(str)

if __name__=="__main__":
    main()