#---Terminal testing for Ex1---
from small_town_teller import Person, Account, Bank
zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)
# 128.02

print()

#---Terminal testing for Ex2---
from persistent_small_town_teller import Person, Account, Bank
zc_bank = Bank()
zc_bank.customers
# {}
zc_bank.accounts
# {}
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_account = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_account)
zc_bank.save_data()

#exit and restart
from persistent_small_town_teller import Person, Account, Bank
zc_bank = Bank()
zc_bank.load_data()
zc_bank.customers
# {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
zc_bank.accounts
# {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}