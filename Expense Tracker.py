# Expense Tracker

balance = 0

def add_income():
    global balance
    amount = float(input("Enter income amount: "))
    balance += amount
    save_to_file("Income", amount)
    print("Income added!")

def add_expense():
    global balance
    amount = float(input("Enter expense amount: "))
    balance -= amount
    save_to_file("Expense", amount)
    print("Expense added!")

def view_balance():
    print("Current Balance:", balance)

def save_to_file(type, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{type}: {amount}\n")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")