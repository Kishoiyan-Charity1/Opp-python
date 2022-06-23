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
        self.transaction=[]
        self.time= datetime.now().strftime('%X')
        self.total=[]
        self.loan_balance=0
        self.loan_repayment=0
        self.transfer=0


    def deposit(self, amount):
        self.balance+=amont
        return f'you have deposited {amount} and your new balance is {self.balance}'

    def deposit(self,amount):
        if amount<=0:
            return f'deposit should be more than zero'
        
        self.balance+=amount
        self.deposits.append({'date':self.time, 'amount':amount, 'narration':'Deposits'})

        return f'you have deposited {amount}, your new balance is {self.balance}', self.Deposits


        # def deposits_statement(self):
        #     for n in self.deposits:
        #         print(f"you have deposited {n} amount of money")
        
        
        

    def withdraw(self,amount):
        
        if amount > self.balance:
            return f'your balance is {self.balance}, you cannot withdraw {amount}'

        elif amount<=0:
            return f'amont must be great than 0'

        else:
            self.transaction_cost=0
            self.balance-=amount + self.transaction_cost
            self.withdrawals.append({'date':self.time, 'amount':amount, 'narration':'withdrawals'})
            return f'you have succeful withdrawed {amount}, your new balance is{self.balance}', self.withdrawals

    def deposits_statement(self):
        for x in self.deposits:
            print(f'you have deposited {x} amount of money')


    def withdraws_statement(self):
        for x in self.withdraws:
            print(f"you have withdrawed {x} amount of money")
  

    def current_balance(self):
        current_balance=self.balance
        return ('your current balance is {balance}')

    def full_statements(self):
        total= self.deposit + self.withdrawals
        for i in total:
            print(i)

    def borrow(self, amount):
        sum=0
        f0r i in self.total:
        sum+=['amount']

        if len(self.deposits) <10:
            print('Deposits must be greater than 10')
        elif amount<100:
            print('amount should be graty than 100')
        elif amount <=(sum//3):
            print('you are qualified for the loan, your balance is {amount}')
        elif self.balance==0:
            print('you can borrow succefully, your account balance is 0')
        elif self.loan_balance > 0:
            print(f'you cannot borrow {amount} clear your previous loan first')
        else:
            self.loan_balance = (0.03*amount)+ amount
            return f'you have succefully borrowed {amount} with an intrest of {0.03*amount}, your new balance is {self.loan_balance}'
   

    def loan_repayments(self, amount):
        loan_repayment = amount - self.loan_balance
        if amount < self.loan_balance:
            return f'you have paid {amount}, and your outstanding balance is {loan_repayment}'
        elif amount == self.loan_balance:
            return 'your have repaid your loan'
        else:
            amount > self.loan_balance
            return f'you have cleared your loan and your new balance is {loan_repayment}'

    def transfer(self, amount, Account2):
        if amount <=0:
            return 'you cannot transfer money'
        elif amont >= self.balance:
            return ' you have insuficient balance'

        else:
            self.balance -=amount
            Account2.balance += amount
            return f'you have transfered {amount} to {Account2} eith name {Account2.account_name}. Your balance is {self.balance}

            
        
      
    

        



