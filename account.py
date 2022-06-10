# from curses import ALL_MOUSE_EVENTS
# from unicodedata import decomposition


class Bank:
    bank_name='kcb'
    def __init__(self,name,acc_number):
        self.name= name
        self.balance= 3000
        self.acc_number= acc_number
        self.deposits=[] 
        self.withdraws=[]


    def deposit(self,amount):
        

        
        
        if amount<=0:
            return f'deposit should be more than zero'
        else:
            self.balance+=amount
            self.deposits.append(amount)
            return f'you have deposited {amount}, your new balance is {self.balance}'

        def deposits_statement(self):
            for n in self.deposits:
                print(f"you have deposited {n} amount of money")
        
        
        

    def withdraw(self,amount):
        

    
        if amount > self.balance:
            return f'your balance is {self.balance}, you cannot withdraw {amount}'

        elif amount<=0:
            return f'amont must be great than 0'

        else:
            self.balance-=amount
            self.withdraws.append(amount)
            return f'you have succeful withdrawed {amount}, your new balance is{self.balance}'

    def withdraws_statement(self):
        for x in self.withdraws:
            print(f"you have withdrawed {x} amount of money")
  

    def current_balance(self):
        current_balance=self.balance
        print (current_balance)
        
      
    

        



