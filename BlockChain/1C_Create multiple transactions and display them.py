class Transaction:
    def __init__(self, transaction_id, date, amount, description):
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount
        self.description = description

    def __str__(self):
        return (f"Transaction ID: {self.transaction_id}, "
                f"Date: {self.date}, "
                f"Amount: ${self.amount:.2f}, "
                f"Description: {self.description}")


def create_transaction():
    transaction_id = input("Enter transaction ID: ")
    date = input("Enter transaction date (YYYY-MM-DD): ")
    amount = float(input("Enter transaction amount: "))
    description = input("Enter transaction description: ")
    return Transaction(transaction_id, date, amount, description)


def display_transactions(transactions):
    if not transactions:
        print("No transactions to display.")
    else:
        print("\nTransaction History:")
        for i, transaction in enumerate(transactions, start=1):
            print(f"{i}. {transaction}")


def main():
    transactions = []
    while True:
        print("\nMenu:")
        print("1. Create a new transaction")
        print("2. Display all transactions")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            transaction = create_transaction()
            transactions.append(transaction)
            print("Transaction added successfully.")
        elif choice == '2':
            display_transactions(transactions)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
