
class Bank:
    def __init__(self, name):
        self.name = name

    def createAccount(self, account_num):
        print(f"Account number {account_num} created")

    def generate_statement(self, customer):
        print(f"Statement for {customer.name}:")
        for account in customer.accounts:
            print(f"Account Number: {account.account_num}, Balance: {account.balance}")

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

class Account:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(("Withdraw", amount))
        else:
            print("Insufficient funds")


my_bank = Bank("MyBank")

gehad = Customer("gehad")
habiba = Customer("habiba")

my_bank.createAccount("123456")
my_bank.createAccount("789012")

gehad_account = Account("123456", 1000)
habiba_account = Account("789012", 500)

gehad.accounts.append(gehad_account)
habiba.accounts.append(habiba_account)

gehad_account.deposit(200)
habiba_account.withdraw(100)

my_bank.generate_statement(gehad)
my_bank.generate_statement(habiba)


