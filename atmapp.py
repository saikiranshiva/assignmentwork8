class LimitExceedException(Exception):
    def __init__(self,var):
        self.var=var

class InvalidMinimumException(Exception):
    def __init__(self,var):
        self.var=var

class InsufficientFundException(Exception):
    def __init__(self,var):
        self.var=var

balance=3200

var=int(input("enter your amount"))
if var >10000:
    raise LimitExceedException("you have entered more then day limit")
elif var < 100:
    raise InvalidMinimumException("yo have entered very less amount enter correct amount")
elif var >balance:
    raise InsufficientFundException("in your account insuuficient funds")
else:
    print("your transaction completes very soon")



