class BankAccount:
    #creating 'routing_number' and 'balance' attributes for class since every object
    #of this class will have the same routing number and a balance of 0 at first
    routing_number = 123123123
    balance = 0

    #init function  created which holds the attributes that are unique to each object of the class
    def __init__(self,full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number

    #deposit function which puts in an 'amount' into the balance and then prints a message telling 
    #you the amount that you've put in
    def deposit(self,amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}.00')

    #withdrawl function which takes out an 'amount' from the balance and then prints a message telling
    #you how much you've takene out. If the amount you take out leaves your balance under 0 then a
    #message will be displayed explaining the insufficient funds and then a $10 overdraft fee will be taken
    #from balance
    def withdraw(self,amount):
        if (self.balance - amount < 0):
            self.balance -= 10
            print(f'Insufficient funds, you now have an overdraft fee of $10.00 on your account. your balance now is ${self.balance}.00')
        else: 
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}.00')
    
    #get_balance function prints a message with the balance and then also returns your full balance
    def get_balance(self):
        print(f'Your account balance is: ${self.balance}')
        return self.balance

    #add_interest function calcultes the interest total and then adds it to the balance
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    #print_receipt function prints out the persons full name, account number, routing number and the balance.
    #The balance is rounded because after adding interest we want to make sure the toal is rounded to the nearest
    #2 decimals
    def print_receipt(self):
        print(f' {self.full_name} \n Account No.: {self.account_number} \n Routing No.: {self.routing_number} \n Balance: ${round(self.balance,2)}')


# John, Steve, Abby are the objects created for the class 
john = BankAccount("John Marcos", 12345678)
steve = BankAccount("Steve Jobs", 35353535)
abby = BankAccount("Abby Flores", 17171717)

john.deposit(30)
john.withdraw(15)
john.get_balance()
john.add_interest()
john.print_receipt()

steve.deposit(15)
steve.withdraw(15)
steve.get_balance()
steve.print_receipt()

abby.deposit(30)
abby.withdraw(31)
abby.get_balance()
abby.add_interest()
abby.print_receipt()
