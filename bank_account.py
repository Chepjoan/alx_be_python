class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with optional starting balance (default 0)."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Deduct amount from balance if sufficient funds exist."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
