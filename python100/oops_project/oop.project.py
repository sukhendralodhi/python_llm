from bank_accounts import *

Dave = BankAccount(2000, "Dave")
Sara = BankAccount(2000, "Sara")

# Dave.get_balance()
# Sara.get_balance()

# Sara.deposit_balance(4000)
# Sara.withdraw(20000)
# Dave.withdraw(90)
# Dave.transfer(1000, Sara)
# Dave.transfer(100, Sara)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)