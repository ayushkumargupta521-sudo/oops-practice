class ATM:
    def __int__(customer):
        customer.name = ""
        customer.pin = ""
        customer.deposit = ""
        customer.withdraw = ""
        customer.balance = ""

    def bank(customer):
        user_input = ("""
        1. Enter Your Name
        2. Set Pin
        3. Deposit
        4. Withdraw
        5. Total Amount
        6. Exit
        """)


        def customer_name(bank):
            customer.name == input("Enter Your Name: ")
            print("Name Entered Successfully")

        def customer_pin(bank):
            customer.pin == int(input("Set Your 4 Digit Pin: "))
            print("Pin Set Successfully")

        def customer_deposit(bank):
            temp = int(input("Enter Your Pin"))
            if temp == customer.pin:
                amount = int(input("Deposit Amount: "))
                if amount < customer.balance:
                    customer.balance = customer.balance - amount
                    print(customer.deposit,"rupee you Deposit in your Account")

        def customer_withdraw(bank):
            customer.withdraw == 