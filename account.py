# from curses import ALL_MOUSE_EVENTS
# from unicodedata import decomposition


class Bank:
    bank_name='kcb'
    def __init__(self,name,number,type,amount):
        self.name= name
        self.number= number
        self.type= type
        self.amount= amount

    def deposit(self,balance):
        self.amount+=balance
        return f'{self.amount}'

    def withdraw(self,balance):
        self.amount-=balance
        return f'{self.amount}'

        



