from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

# Dave.get_balance()
# Sara.get_balance()

# Sara.deposit_balance(4000)
# Sara.withdraw(20000)
# Dave.withdraw(90)
Dave.transfer(100, Sara)