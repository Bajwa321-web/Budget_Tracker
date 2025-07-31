# Budget Tracker CLI App
from datetime import datetime

# Validates date and time ⌚ using strptime 
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
#  📋 Lists to store income and expense entries 
income = []
expenses = []

# Adds a new income entry 💵
def add_income():
    try:
        amount = float(input("💰 Enter income amount (₹): "))
        if amount <= 0:
            print("⚠️ Amount should be greater than 0.\n")
            return
        source = input("🏦 Enter source of income: ").title()
        date = input("📅 Enter date (YYYY-MM-DD): ")
        if not is_valid_date(date):
            print("⚠️ Invalid date format. Please use YYYY-MM-DD.\n")
            return

        income_entry = {
            "Amount": amount,
            "Source": source,
            "Date": date
        }

        income.append(income_entry)
        print("✅ Income added successfully!\n")

    except ValueError:
        print("⚠️ Invalid amount. Please enter numbers only.\n")

# Adds a new expense entry 💸
def add_expense():
    try:
        amount = float(input("💸 Enter expense amount (₹): "))
        if amount <= 0:
            print("⚠️ Amount should be greater than 0.\n")
            return
        category = input("📂 Enter category (e.g. Food, Travel): ").title()
        date = input("📅 Enter date (YYYY-MM-DD): ")
        if not is_valid_date(date):
            print("⚠️ Invalid date format. Please use YYYY-MM-DD.\n")
            return

        expense = {
            "Amount": amount,
            "Category": category,
            "Date": date
        }

        expenses.append(expense)
        print("✅ Expense added successfully!\n")

    except ValueError:
        print("⚠️ Invalid amount. Please enter numbers only.\n")

# Views all recorded expenses 📊
def view_expenses():
    if not expenses:
        print("📭 No expenses recorded yet.\n")
        return

    print("\n🧾 Your Expenses:")
    print("-" * 30)

    index = 1
    for expense in expenses:
        print(f"{index}. ₹{expense['Amount']} | {expense['Category']} | {expense['Date']}")
        index += 1

    print("-" * 30 + "\n")

# Views all recorded income 🏦
def view_income():
    if not income:
        print("📭 No income recorded yet.\n")
        return

    print("\n🏦 Your Income:")
    print("-" * 30)

    for i, entry in enumerate(income, start=1):
        print(f"{i}. ₹{entry['Amount']} | {entry['Source']} | {entry['Date']}")

    print("-" * 30 + "\n")

#View financial balance 📈
def view_balance():
    total_income = sum(entry["Amount"] for entry in income)
    total_expenses = sum(entry["Amount"] for entry in expenses)
    balance = total_income - total_expenses

    print("\n📈 Financial Summary:")
    print(f"💰 Total Income: ₹{total_income}")
    print(f"💸 Total Expenses: ₹{total_expenses}")
    print(f"🧮 Net Balance: ₹{balance}\n")


# Displays the main menu for the Expense Manager 🗂️
def show_menu():
    print("\nExpense Manager")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. View Income")
    print("5. View Balance")
    print("6. Exit")

# Main function to run the Expense Manager CLI App 🚀
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            # Code to add income
            add_income()
        elif choice == "2":
            # Code to add expense
            add_expense()
        elif choice == "3":
            # Code to view expenses
            view_expenses()
        elif choice == "4":
            # Code to view income
            view_income()
        elif choice == "5":
            # Code to view balance
            view_balance()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()