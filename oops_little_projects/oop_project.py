from bank_accounts import *

Div0 = BankAccount(1000, "Div")
Div1 = BankAccount(2000, "Div1")

Div0.getBalance()
Div1.getBalance()

Div1.deposit(500)

Div0.withdraw(10000)
Div0.withdraw(10)

Div0.transfer(1000, Div1)
Div0.transfer(900, Div1)

#Another account name Tom

Tom = IntrestRewardsAcct(1000, "Tom")
Tom.getBalance()

Tom.deposit(100)

Tom.transfer(100, Div1)

#Another account Dip

Dip = SavingsAcct(1000, "Dip")

Dip.getBalance()

Dip.deposit(100)

Dip.transfer(10000, Div0)
Dip.transfer(1000, Div0)
