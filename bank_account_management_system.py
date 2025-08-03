from datetime import datetime
from abc import abstractmethod


class Account:
    bank_name = "Bank of Baroda"
    minimum_balance = 200
    total_accounts = 0
    total_balance = 0
    
    @classmethod
    def set_bank_name(cls,new_name):
        cls.bank_name = new_name
    
    @classmethod
    def set_minimum_balance(cls,new_minimum_balance):
        cls.minimum_balance = new_minimum_balance
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
    @abstractmethod
    def __generate_account_number(self):
        """Generate unique account number"""
        # return f"ACC{BankAccount.total_accounts + 1:06d}"
        pass
    
    def __init__(self,account_number, account_holder, initial_balance=0):
        # Instance variables
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Account number must be a non-empty string.")
        if not account_holder or not isinstance(account_holder, str):
            raise ValueError("Account holder name must be a non-empty string.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.created_date = datetime.now()

        # Update class variables
        Account.total_accounts += 1
        Account.total_balance += initial_balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} successfully.")
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"Withdrawal of {amount} successfully.")
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account number: {self.account_number}, Account holder: {self.account_holder}, Balance: {self.balance}"
    



class SavingsAccount(Account):
    def __init__(self,account_number, account_holder, initial_balance=0, interest_rate = 2.5):
        super().__init__(account_number,account_holder, initial_balance)
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = interest_rate
    
    def withdraw(self, amount):
        try:
            if (self.balance - amount) >= self.minimum_balance:
                return super().withdraw(amount)
        except e as Exception:
            print('Error: Not allowed to withdraw beyond minimum balance limit.')

    def calculate_monthly_interest(self):
        current_balance = self.balance
        interest_rate = self.interest_rate
        monthly_rate = interest_rate/12
        interest = current_balance * (monthly_rate/100)
        return round(interest,2)

class CheckingAccount(Account):
    def __init__(self,account_number, account_holder, initial_balance=0, overdraft_limit = 100):
        super().__init__(account_number, account_holder, initial_balance)
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        try:
            if amount <= (self.balance + self.overdraft_limit):
                return super().withdraw(amount)
        except Exception as e:
            print('Error: Overdraft limit exceeded.')




# Test Case 1: Creating different types of accounts
savings_account = SavingsAccount("SA001", "Alice Johnson", 1000, 2.5)
checking_account = CheckingAccount("CA001", "Bob Smith", 500, 200)

print(f"Savings Account: {savings_account}")
print(f"Checking Account: {checking_account}")

# Test Case 2: Deposit and Withdrawal operations
print(f"Savings balance before: ${savings_account.get_balance()}")
savings_account.deposit(500)
print(f"After depositing $500: ${savings_account.get_balance()}")

withdrawal_result = savings_account.withdraw(200)
print(f"Withdrawal result: {withdrawal_result}")
print(f"Balance after withdrawal: ${savings_account.get_balance()}")

# Test Case 3: Overdraft protection in checking account
print(f"Checking balance: ${checking_account.get_balance()}")
overdraft_result = checking_account.withdraw(600)  # Should use overdraft
print(f"Overdraft withdrawal: {overdraft_result}")
print(f"Balance after overdraft: ${checking_account.get_balance()}")

# Test Case 4: Interest calculation for savings
interest_earned = savings_account.calculate_monthly_interest()
print(f"Monthly interest earned: ${interest_earned}")

# Test Case 5: Class methods and variables
print(f"Total accounts created: {Account.get_total_accounts()}")
print(f"Bank name: {Account.bank_name}")

# Change bank settings using class method
Account.set_bank_name("New National Bank")
Account.set_minimum_balance(100)

# Test Case 6: Account validation
try:
    invalid_account = SavingsAccount("SA002", "", -100, 1.5)  # Should raise error
except ValueError as e:
    print(f"Validation error: {e}")

# Expected outputs should show proper account creation, transaction handling,
# interest calculation, and class-level operations
