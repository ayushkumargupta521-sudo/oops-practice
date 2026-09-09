class student:

    def __init__(self):
        self.name = ""
        self.roll = ""
        self.detail = ""
        self.stream = ""
        # self.exit = ""

    def menu(self):
        user_input = input(""" 
1 - Enter Your Name
2 - Enter Your Roll Number
3 - Parents Detail
4 - Stream
5 - Exit
""")
        if user_input == "1":
            self.your_name()
            
        elif user_input == "2":
            self.roll_no()
            
        elif user_input == "3":
            self.parents_detail()
            
        elif user_input == "4":
            self.branch()
        else:
            self.exit()


    def your_name(self):
        self.name = input("Enter your Name: ")
        print("Name Entered Successfully")

    def roll_no(self):
        self.roll = int(input("Enter Roll Number: "))
        print("Roll Number Entered Successfully")

    def parents_detail(self):
        self.stream = input("Enter Your Parent Name: ")
        print("Parent Name Entered Successfully")

    def branch(self):
        self.detail = input("Enter Your Stream/Branch: ")
        print("Entered Stream Successfully")    

    def exit(self):
        print("Exit")
s1 = student()
s1.menu()
