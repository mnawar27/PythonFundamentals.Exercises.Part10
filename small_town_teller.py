class Person:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

class Account:

    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

class Bank:

    def __init__(self):
        self.customers = {}

    def addCustomer(self, id, first_name, last_name):
        if id in self.customers:
            print("already exists!")
        else:
            new_customer = Person(id,first_name, last_name)
            self.customers[id] = new_customer
            print(f"Added customer: {new_customer}")

    def addAccount():
        pass

    def removeAccount():
        pass

    def deposit():
        pass

    def withdraw():
        pass

    def balance():
        pass


