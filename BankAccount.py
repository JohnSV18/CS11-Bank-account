class BankAccount:
    routing_number = 123123123
    balance = 0
    def __init__(self,full_name, account_number):
        self.full_name = full_name
        self.account_number = account_number

    def deposit(self,amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}.00')

    def withdraw(self,amount):
        
        if (self.balance - amount < 0):
            self.balance -= 10
            print(f'Insufficient funds, you now have an overdraft fee of $10.00 on your account. your balance now is ${self.balance}.00')
        else: 
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}.00')
   
    def get_balance(self):
        print(f'Your account balance is ${self.balance}.00')
        # return (f'{self.balance}')

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_receipt(self):
        print(f' {self.full_name} \n Account No.:{self.account_number} \n Routing No.:{self.routing_number} \n Balance:${self.balance}.00 ')




    



john = BankAccount("John Marcos", 12345678)
steve = BankAccount("Steve Jobs", 35353535)
abby = BankAccount("Abby Flores", 17171717)
