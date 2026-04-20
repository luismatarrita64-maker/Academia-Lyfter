class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def DepositMoney(self):
        try:
            money = float(input("Enter money to deposit: "))
        except ValueError:
            raise ValueError("Input must be a number.")

        if money < 0:
            raise ValueError("Amount cannot be negative.")

        self.balance += money
        print(f"Deposit successful. New balance: {self.balance}")

    def RetireMoney(self):
        print(f"Current balance: {self.balance}")

        try:
            money = float(input("Money to withdraw: "))
        except ValueError:
            raise ValueError("Input must be a number.")

        if money < 0:
            raise ValueError("Amount cannot be negative.")

        if money > self.balance:
            raise ValueError("Insufficient funds.")
        
        self.balance -= money
        print(f"Withdrawal successful. New balance: {self.balance}")


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def RetireMoney(self):
        print(f"Current balance: {self.balance}")

        try:
            money = float(input("Money to withdraw: "))
        except ValueError:
            raise ValueError("Input must be a number.")

        if money < 0:
            raise ValueError("Amount cannot be negative.")


        if self.balance - money < self.min_balance:
            raise ValueError("Cannot withdraw: would fall below minimum balance.")

        self.balance -= money
        print(f"Withdrawal successful. New balance: {self.balance}")

AC = SavingsAccount(300, 50)
AC.DepositMoney()
AC.RetireMoney()