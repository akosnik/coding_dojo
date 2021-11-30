class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount=0):
        self.balance += amount
        return self

    def withdraw(self, amount=0):
        if (self.can_withdraw(self.balance, amount)):
            self.balance -= amount
        return self

    def display_account_info(self, user_name='', acct_name=''):
        print(user_name, acct_name, self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)  # right side evaluates to 1.02
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
            print("Insufficient Funds")
        else:
            return True

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


class User:
    user_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        self.default_account = self.new_account(
            balance=500)  # $500 sign up bonus
        User.user_count += 1

    def new_account(self, acct_name="Checking", int_rate=0.02, balance=0):
        self.accounts[acct_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, acct_name, amount=0):
        self.accounts[acct_name].deposit(amount)
        return self

    def make_withdrawl(self, acct_name, amount=0):
        self.accounts[acct_name].withdraw(amount)
        return self

    def display_user_balance(self, acct_name):
        self.accounts[acct_name].display_account_info(self.name, acct_name)
        return self

    def display_user_all_balances(self):
        for acct_name in self.accounts.keys():
            self.display_user_balance(acct_name)
        return self

    @classmethod()
    def transfer_balance(cls, sender, withdrawl_account, recipient, deposit_account, amount=0):
        sender.make_withdrawl(withdrawl_account, amount)
        recipient.make_deposit(deposit_account, amount)
        return self


pip = User("Pip", "pip@cool.com")

pip.new_account("Savings", 0.04).make_deposit(
    "Savings", 6000).make_deposit("Checking", 1000)

smokey = User("Smokey", "smokey@cool.com")

User.transfer_balance(pip, "Checking", smokey, "Checking", 10)

pip.display_user_all_balances()
smokey.display_user_all_balances()
