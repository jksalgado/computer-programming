#Bank Account Lab
#Jasmin Salgado
#3/18/21

#class called BankAccount
class BankAccount():
    """bank account class"""
    interestRate = .0125
    nextAccountNumber = 12345
    
    def __init__(self, name, balance):
        self.accountNumber = BankAccount.nextAccountNumber
        self.name = name
        self.balance = balance
        BankAccount.nextAccountNumber += 1

    def deposit(self, amount):
        """adding the amount deposited to the balance"""
        self.balance += amount
        print(f"balance after DEPOSIT or DEPOSIT OF INTEREST: ${self.balance}")

    def withdraw(self, amount):
        """removing money from the balance"""
        if self.balance > amount:
            self.balance -= amount
            print(f"balance after WITHDRAW: ${self.balance}")
        else:
            print("ACTION NOT COMPLETE: OVERDRAW, NOT ENOUGH MONEY TO WITHDRAW")

    def depositInterest(self):
        """adding the interest amount to the balance"""
        self.deposit(self.balance * BankAccount.interestRate)

    def transferFunds(self, BankAccount, amount):
        """transfering money to another account"""
        if self.balance > amount:
            self.balance -= amount
            BankAccount.balance += amount
            print(f"Your balance after TRANSFER: {self.balance}\nOther balance after TRANSFER: {BankAccount.balance}")
        else:
            print("ACTION NOT COMPLETE: NOT ENOUGH MONEY TO TRANFER TO ACCOUNT")

    def __str__(self):
        display = "\nAccount Number: " + str(self.accountNumber) + "\n"
        display += "Account Name: " + str(self.name) + "\n"
        display += "Balance: " + str(self.balance) + "\n"
        return display
        

#ACCOUNT 1
a1 = BankAccount("Jasmin Salgado", 1000)
print(a1)
a1.deposit(500)
a1.withdraw(200)
a1.depositInterest()

#ACCOUNT 2
a2 = BankAccount("Bob Ross", 2000)
print(a2)
a2.deposit(100)
a2.withdraw(3000)
a2.depositInterest()

#TRANSFERING 
a1.transferFunds(a2,1000)
a2.transferFunds(a1,5000)

