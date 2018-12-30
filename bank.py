#Project about setting up banking issues, adding a deposit/savings to a user, withdraw and statement using python 3.7.2
#Z = Current("Vanessa", 300) press enter
#Z.deposit(300)
#Z.statement()
#it will show 800 balance!

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance +=  amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: £{}".format(self.balance))
        
#class current inherit the class account (data object)
class Current(Account):
    #constructor in python
    def __init__(self, name, balance):
        #call the parent Account set we want in the current class
        super().__init__(name, balance, min_balance = -1000 )
        
    #defines what it display in the screen
    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)

class Savings(Account):
    def __init__(self, name, balance):
        #call the parent Account set we want in the savings class
        super().__init__(name, balance, min_balance = 0)

    #defines what it display in the screen
    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance)

    
