class Account:
    def __init__(self,accno,accname,acctype):
        self.accountno=accno
        self.accountname=accname
        self.accounttype=acctype

    def withdraw(self,bal, amount):
        if (bal < amount):
            raise LowBalanceException("balance is not sufficient")
