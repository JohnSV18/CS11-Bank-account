class BankAccount:
    routing_number = 123123123
    def __init__(self,full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = 0