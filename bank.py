class Bank:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        
        print("1. Create Pin")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        user_input = input("Please select an option: ")

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.check_balance()
        elif user_input == "3":
            self.deposit()
        elif user_input == "4":
            self.withdraw()
        elif user_input == "5":
            print("Thank you for using our services.")
        else:
            print("Invalid option. Please try again.")
            self.menu()
    def create_pin(self):
        self.pin = input("Please create a 4-digit PIN: ")
        if len(self.pin) == 4 and self.pin.isdigit():
            print("PIN created successfully.")
        else:
            print("Invalid PIN. Please try again.")
            self.create_pin()
        self.menu()
    def check_balance(self):
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == self.pin:
            print(f"Your balance is: ${self.balance}")
        else:
            print("Incorrect PIN. Please try again.")
            self.check_balance()
        self.menu()
    def deposit(self):
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"${amount} deposited successfully. Your new balance is: ${self.balance}")
            else:
                print("Invalid amount. Please try again.")
                self.deposit()
        else:
            print("Incorrect PIN. Please try again.")
            self.deposit()
        self.menu()
    def withdraw(self):
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter the amount to withdraw: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully. Your new balance is: ${self.balance}")
            else:
                print("Invalid amount or insufficient funds. Please try again.")
                self.withdraw()
        else:
            print("Incorrect PIN. Please try again.")
            self.withdraw()
        self.menu()
if __name__ == "__main__":
    bank = Bank()