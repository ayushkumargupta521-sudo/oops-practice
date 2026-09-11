class ATM:
    def __init__(self):
        self.name = ""
        self.pin = 0
        self.deposit = 0
        self.withdraw = 0

    def bank(self):
        user_input = input("""
        1 - Name
        2 - PIN
        3- Deposit
        4 - withdraw
        """)


        if user_input == "1":
                    self.your_name()
    
        elif user_input == "2":
                    self.set_pin()
        
        elif user_input == "3":
                    self.amount_deposit()
        
        elif user_input == "4":
                    self.amount_withdraw()
        else:
            print("Exit")

    def your_name(self):
        self.name = input("Enter Your Name: ")
        print(self.name," is your Name")

    def set_pin(self):
        self.pin = int(input("Set your PIN"))
        print("PIN Set Successfully")

    def amount_deposit(self):
        self.deposit = int(input("Deposit Your Money: "))
        print("Successfully Deposit")



c1 = ATM()
c1.bank()