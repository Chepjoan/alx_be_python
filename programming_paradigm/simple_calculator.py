class BankAccount:
    """A simple BankAccount class to manage deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient balance exists."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current balance with two decimal places."""
        print(f"Current Balance: ${self.balance:.2f}")
