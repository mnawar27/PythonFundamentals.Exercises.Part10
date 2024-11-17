class Person:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account:

    def __init__(self, number, type, owner, balance=0):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance
    
class Bank:

    def __init__(self):
        self.customers = {}
        self.accounts = {}


    #---Adding a customer---
    def add_customer(self, customer):
        if customer.id in self.customers:
            print("already exists!")
        else:
            self.customers[customer.id] = customer
            print(f"Added customer: {customer.first_name} {customer.last_name}(ID: {customer.id})")



    #--Adding an account--
    def add_account(self, account):
        if account.number in self.accounts:
            print("already exist!")
        elif account.owner.id  not in self.customers:
            print("customer id not found")
        else:
            self.accounts[account.number] = account
            print(f"Added account: Account Number: {account.number}, Type: {account.type}, Balance: ${account.balance}")



    #---Removing an account---
    def remove_account(self, account):
        if account.number in self.accounts:
            self.accounts.pop(account.number)
            print("Account removed")
        else:
            print("account doesn't exist")



    #---Depositing money---
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount > 0:
                account.balance += amount
                print(f"Deposit successful! Deposited ${amount}")
            else:
                print("must be greater than zero")
        else:
            print("account doesn't exist")



    #---Withdrawing money---
    def withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            if amount > 0 and amount <= account.balance:
                account.balance -= amount
                print(f"Withdraw successful! Withdrew ${amount}")
            elif amount <= 0:
                print("must be greater than zero.")
            else:
                print("Insufficient funds.")
        else:
            print("account doesn't exist")



    #---Balance inquiry---
    def balance_inquiry(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("account doesn't exist")