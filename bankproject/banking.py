from abc import ABC, abstractmethod

# Abstract Base Class
class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance   # encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited {amount}. New Balance = {self.__balance}")
        else:
            print("❌ Invalid deposit amount")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance

    def _update_balance(self, new_balance):  # protected helper
        self.__balance = new_balance


# Savings Account (with min balance rule)
class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, min_balance=500):
        super().__init__(account_number, owner, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.min_balance:
            self._update_balance(self.get_balance() - amount)
            print(f"💸 Withdrawn {amount}. New Balance = {self.get_balance()}")
        else:
            print("⚠️ Cannot withdraw! Minimum balance requirement not met.")


# Current Account (with overdraft allowed)
class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=1000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.overdraft_limit:
            self._update_balance(self.get_balance() - amount)
            print(f"💸 Withdrawn {amount}. New Balance = {self.get_balance()}")
        else:
            print("⚠️ Overdraft limit exceeded!")


# ------------------- MAIN MENU ------------------- #
if __name__ == "__main__":
    accounts = {}

    while True:
        print("\n==== Banking System Menu ====")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            accounts[acc_no] = SavingsAccount(acc_no, name, balance)
            print("✅ Savings Account Created!")

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            accounts[acc_no] = CurrentAccount(acc_no, name, balance)
            print("✅ Current Account Created!")

        elif choice == "3":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter Deposit Amount: "))
                accounts[acc_no].deposit(amount)
            else:
                print("❌ Account not found!")

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                amount = float(input("Enter Withdrawal Amount: "))
                accounts[acc_no].withdraw(amount)
            else:
                print("❌ Account not found!")

        elif choice == "5":
            acc_no = input("Enter Account Number: ")
            if acc_no in accounts:
                print(f"💰 Balance = {accounts[acc_no].get_balance()}")
            else:
                print("❌ Account not found!")

        elif choice == "6":
            print("👋 Exiting Banking System. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")
