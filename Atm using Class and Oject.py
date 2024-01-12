class Atm:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()
    
    def menu(self):
        try:
            user_input = int(input("""
            How can I help you?
            1. Press 1 for create pin
            2. Press 2 for change pin 
            3. Press 3 for check balance 
            4. Press 4 to withdraw
            5. Press 5 for exit : 
            """))

            if user_input == 1:
                # create pin
                self.create_pin()
            elif user_input == 2:
                # change pin
                self.change_pin()
            elif user_input == 3:
                # check balance
                self.check_balance()
            elif user_input == 4:
                # withdraw amount 
                self.withdraw()
            elif user_input == 5:
                # exit the code
                exit()
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
                self.menu()

        except ValueError:
            print("Please enter a valid integer.")
            self.menu()

    def create_pin(self):
        user_pin = int(input("Enter your pin: "))
        self.pin = user_pin
        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance
        print("Pin generated successfully")
        self.menu()
    
    
    def change_pin(self):
        old_pin=int(input("Enter your old pin : "))
        if old_pin==self.pin:
            new_pin=int(input("Enter your new pin : "))
            self.pin=new_pin
            print("Pin changed successfully")
        else:
            print("Please enter correct pin")
        self.menu()
    
    def check_balance(self):
        pin=int(input("Enter your pin : "))
        if pin==self.pin:
            print(f"your balance is : {self.balance}")
        else:
            print("Please enter correct pin ")
        self.menu()
    
    def withdraw(self):
        pin=int(input("Enter your pin : "))
        if pin==self.pin:
            money=int(input("how many rupess you want to withdraw : "))
            if money<=self.balance:
                withdraw_amount=money
                print(f"Successfully withdraw amount {withdraw_amount}")
                self.balance=self.balance-withdraw_amount
                print(f"your remaining amount in your ac is {self.balance}")
            else:
                print("Not enogh money")
        else:
            print("Enter correct pin")
        self.menu()

user1 = Atm()