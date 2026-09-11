class ATM:
    def __init__(self):
        self.name = ""
        self.pin = 0
        self.deposit = 0
        self.withdraw = 0
        self.balance = 0

    def your_name(self):
        self.name = input("Enter Your Name: ")
        print(self.name," is your Name")

    def set_pin(self):
        while True:
            user_pin = input("Set your 4-digit PIN: ")
            if len(user_pin) == 4 and user_pin.isdigit():
                self.pin = user_pin
                print("PIN Set Successfully")
                break
            else:
                print("Invalid PIN! PIN must be exactly 4 digits.")

    def amount_deposit(self):
        temp = int(input("Enter Your PIN: "))
        if temp == self.pin:
               amount = int(input("Deposit Money: "))
               self.balance = self.balance + amount
               print(amount,"rupee Deposit Successfully")
               print(self.balance,"is Your Total Amount")
        else:
               print("Enter PIN Again")

    def amount_withdraw(self):
        temp = int(input("Enter ATM PIN"))
        if temp == self.pin:
            withdraw_amount = int(input("Enter withdraw amount: "))
            if withdraw_amount < self.balance:
                self.balance = self.balance - withdraw_amount
                print(withdraw_amount," rupee withdraw")
                print("Remaining Balance:", self.balance, "rupee")
            else:
                print("Insufficient Balance",self.balance,"rupee is Balance")
                print(self.balance,"rupee is Balance")
        else:
            print("Enter PIN Again")

    def bank(self):
        while True:
            user_input = input("""
            1. Enter Your Name
            2. Set Pin
            3. Deposit
            4. Withdraw
            5. Total Amount
            6. Exit
            Select Option:
            """)


            if user_input == "1":
                self.your_name()
    
            elif user_input == "2":
                self.set_pin()
        
            elif user_input == "3":
                self.amount_deposit()
        
            elif user_input == "4":
                self.amount_withdraw()

            elif user_input == "5":
                print("Total Amount is :", self.balance)
            elif user_input == "6":
                print("Exit")
                break
            else:
                if user_input >= "7":
                    print("Invalid Syntax Choose from 1 - 6")

c1 = ATM()
c1.bank()