expenses = []

def add_expense():
    print("\n Add Expense")
    category = input("Enter category (Food/Travel/Bills/Others): ")
    amount = float(input("Enter amount: "))
    note = input("Enter a note (optional): ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    print("\n All Expenses")
    if not expenses:
        print("No expenses recorded.\n")
        return

    total = 0
    for e in expenses:
        print(f"Category: {e['category']}, Amount: {e['amount']}, Note: {e['note']}")
        total += e["amount"]
    print(f"Total Spent: {total}\n")


def summary_by_category():
    print("\n Expense Summary by Category")
    if not expenses:
        print("No expenses recorded.\n")
        return

    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    for cat, amt in summary.items():
        print(f"{cat}: {amt}")
    print()


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()