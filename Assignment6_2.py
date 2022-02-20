import getpass


OBJ = 1200987


def Create_Account():
    ACCOUNT_NUMBER = 5454154
    ACCOUNT_NUMBER += 1
    global OBJ, Mobile_No, Pass
    OBJ += 1
    flag = True;
    val = False;
    Value = False
    SpecialSym = ['$', '@', '#', '%', '&', '~']
    print(''' \t   Welcome To Bank Of Marvellous \n
Fill Following Details For Create Account \n''')

    C_Name = input('Enter Your Full Name : ')

    while (val != True):
        Mobile_No = int(input('Enter Your Mobile Number Here : '))
        Con_Str = str(Mobile_No)

        if len(Con_Str) == 10:
            val = True
            E_Id = input('Enter Email Id : ')
            Pan_No = input('Enter Your PAN Card Number : ')
        else:
            print('Enter Correct Mobile Number')
    NUM = 0
    while NUM != 6:
        NUM = 0
        Pass = getpass.getpass('Enter Password : ')

        if len(Pass) < 7:
            print('Password length should be at least 8 ')
        else:
            NUM += 1
        if len(Pass) > 20:
            print('Password length should not be greater than 20')
        else:
            NUM += 1
        if not any(char.isdigit() for char in Pass):
            print('password should contain at least 1 Numeral ')
        else:
            NUM += 1
        if not any(char.isupper() for char in Pass):
            print('Password should contain at least 1 upper case letter')
        else:
            NUM += 1
        if not any(char.islower() for char in Pass):
            print('Password should contain at least one lover case lettar')
        else:
            NUM += 1
        if not any(char in SpecialSym for char in Pass):
            print('Password should contain at least 1 Special Symbol')
        else:
            NUM += 1
        # print('Val Of NUM is ',NUM)
        R_Val = False
        try:
            while not R_Val:
                Re_Entered_Pass = input('Confirm Password : ')
                if Pass == Re_Entered_Pass:
                    # paswd = Pass
                    print('Your password is : ', Pass)
                    print('Your Account Number Is : ', ACCOUNT_NUMBER)
                    print('Thank You {0} Good Luck {1}  '.format("\U0001F64F", "\U0001F609"))
                    print('\tACOUNT SUCCESSFULLY GETS CREATED...')
                    R_Val = True
                else:
                    print("You Entered Wrong Password ")
        except UnboundLocalError as obj1:
            print('Exception Staement is : ', obj1)

    return C_Name, Mobile_No, OBJ, Pass, ACCOUNT_NUMBER


ROI = 10.5


class BankAccount:

    def __init__(self, a_name):
        global ROI
        self.Name = a_name
        self.Amount = 0.0
        self.Intrest_Cal = 0.0

    def Deposit(self, Account_Num, Passwd):
        Limit = False;
        Lim = 0
        print('For Deposit Amount Please Fill Following Details ')
        AC_Num = int(input('Enter Your Account Number : '))
        if AC_Num == Account_Num:

            while (
                    Limit != True and Lim != 5):  # Password  Attempt Limit is. After Attempting 5 triel it'll
                # terminate function
                Lim += 1
                PassWord = input('Enter Your Password : ')
                if PassWord == Passwd:
                    Deposit_Amount = float(input('Please Enter Amount to Deposit : '))
                    self.Amount += Deposit_Amount
                    Limit = True
                else:
                    print('Enter Valid Password')
        else:
            print('Enter Valid Account Number ')
            return

    def Widrawal(self, Account_Num, Passwd):
        Permission = False;
        LimX = 0
        print('For Withdrawal Amount Please Fill Following Details ')
        AC_Num = int(input('Enter Your Account Number : '))
        if AC_Num == Account_Num:

            while Permission != True and LimX != 5:  # Password Limit is 5
                LimX += 1
                PassWord = input('Enter Your Password : ')
                if PassWord == Passwd:
                    Deposit_Amount = float(input('Please Enter Amount to Deposit : '))
                    self.Amount += Deposit_Amount
                    Permission = True
                else:
                    print('Enter Valid Password')
                self.Amount -= Deposit_Amount
        else:
            print('Enter Valid Account Number')
            return

    def CalculateIntrest(self, Account_Num, Passwd):
        PassWord = input('Enter Your Password : ')
        if PassWord == Passwd:
            self.Intrest_Cal = (self.Amount * ROI) / 100
            print('Intrest On Your Amount is {} '.format(self.Intrest_Cal))
        else:
            print('Enter Valid Details')
            return

    def Display(self, Account_Num, Passwd, Phon_Num):
        PassWord = input('Enter Your Password : ')
        if PassWord == Passwd:
            print('Account Holder Name Is : {} '.format(self.Name))
            print('Your Account Balance Is : {} '.format(self.Amount))
            print('Mobile Number is : ', Phon_Num)


def main():
    Cust_Name, Phone_No, ac_name, PaswdX, Account_Number = Create_Account()
    ac_name = BankAccount(Cust_Name)

    while True:
        print('''         
      Please Choose Following Options For Transation
        
            1. Deposite
            2. Widrawal
            3. Calculate Intrest
            4. Display
            0. Terminate Application  
            ''')
        Choice = int(input('enter the Choice : '))
        if Choice >= 0 and Choice <= 5:
            if Choice == 1:
                ac_name.Deposit(Account_Number, PaswdX)
            elif Choice == 2:
                ac_name.Widrawal(Account_Number, PaswdX)
            elif Choice == 3:
                ac_name.CalculateIntrest(Account_Number, PaswdX)
            elif Choice == 4:
                ac_name.Display(Account_Number, PaswdX, Phone_No)
            elif Choice == 0:
                break
        else:
            print('Enter Valid choice')


if __name__ == "__main__":
    main()
