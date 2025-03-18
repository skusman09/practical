class Transaction:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def send_money(self, amount, recipient):
        if amount <= 0:
            return "Amount must be greater than zero."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        recipient.receive_money(amount)
        return f"Sent {amount} to {recipient.account_holder}. Remaining balance: {self.balance}."

    def receive_money(self, amount):
        """Receive money from another account."""
        if amount <= 0:
            return "Amount must be greater than zero."
        self.balance += amount
        return f"Received {amount}. New balance: {self.balance}."

    def __str__(self):
        """Return account details as a string."""
        return f"Account Holder: {self.account_holder}, Balance: {self.balance}"


# Test function to verify the Transaction class
def test_transaction():
    alice_account = Transaction("Alice", 1000)
    bob_account = Transaction("Bob", 500)

    print("Initial Accounts:")
    print(alice_account)
    print(bob_account)

    # Test 1: Alice sending money to Bob
    print("\nTest 1: Alice sends money to Bob")
    print(alice_account.send_money(200, bob_account))

    print("\nUpdated Accounts:")
    print(alice_account)
    print(bob_account)

    # Test 2: Bob trying to send more money than he has
    print("\nTest 2: Bob tries to send more money than he has")
    print(bob_account.send_money(800, alice_account))

    # Test 3: Bob sending money to Alice
    print("\nTest 3: Bob sends money to Alice")
    print(bob_account.send_money(100, alice_account))

    print("\nFinal Accounts:")
    print(alice_account)
    print(bob_account)


# Run the test function
test_transaction()
