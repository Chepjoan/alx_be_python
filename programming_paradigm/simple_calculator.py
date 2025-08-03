class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtract amount from balance if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount

    def display_balance(self):
        """Display the current balance with two decimal places."""
        print(f"Current Balance: ${self.balance:.2f}")
