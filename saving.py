class Bank:
    def__init__(self,accountname, accountnumber):
        self.accountname = accountname
        self.accountnumber= accountnumber
        self.balance=0

def deposit(self, amount):
    if amount <=0:
        return 'you cannot deposit bellow 0'
    elif amount <5:
        return f'you cannot deposit bellow 50'
    else:
        self.balance+=amount
        return f'you have deposited {amount} your current balance is {self.balance}'

def withdrawal(self,amount):
    if amount <=0:
        return f'you cannot withdraw less thann 0'
    elif: amount < 100:
        return f'you cannot withdraw less than a 100'
