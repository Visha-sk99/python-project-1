import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
def init_csv():
    if not os.path.exists("finance.csv"):
        df = pd.DataFrame(columns=["Date", "Type", "Amount", "Category", "Note"])
        df.to_csv("finance.csv", index=False)
def add_entry():
    entry_type = input("Enter type (Income/Expense): ").capitalize()
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Rent, Salary, etc.): ").capitalize()
    note = input("Optional note: ")

    date = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame([[date, entry_type, amount, category, note]],
                            columns=["Date", "Type", "Amount", "Category", "Note"])

    new_data.to_csv("finance.csv", mode='a', index=False, header=False)
    print("\n✅ Entry added successfully!\n")
def view_transactions():
    df = pd.read_csv("finance.csv")
    print("\n--- All Transactions ---\n")
    print(df)
def show_summary():
    df = pd.read_csv("finance.csv")

    total_income = df[df['Type'] == 'Income']["Amount"].sum()
    total_expense = df[df['Type'] == 'Expense']["Amount"].sum()
    balance = total_income - total_expense

    print(f"\n💰 Total Income  : ₹{total_income:.2f}")
    print(f"💸 Total Expense : ₹{total_expense:.2f}")
    print(f"📊 Balance       : ₹{balance:.2f}")
def plot_expense_pie():
    df = pd.read_csv("finance.csv")
    expenses = df[df['Type'] == 'Expense']

    if expenses.empty:
        print("\n⚠️ No expense data to show.\n")
        return

    cat_sum = expenses.groupby("Category")["Amount"].sum()
    cat_sum.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(6,6))
    plt.title("🧾 Expense Distribution by Category")
    plt.ylabel("")
    plt.show()
def plot_monthly_bar():
    df = pd.read_csv("finance.csv")
    df["Month"] = pd.to_datetime(df["Date"]).dt.strftime('%Y-%m')

    grouped = df.groupby(["Month", "Type"])["Amount"].sum().unstack().fillna(0)
    grouped.plot(kind='bar', figsize=(10,6))
    plt.title("📅 Monthly Income vs Expenses")
    plt.ylabel("Amount (₹)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def menu():
    init_csv()
    while True:
        print("\n========= PERSONAL FINANCE TRACKER =========")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Category-wise Pie Chart")
        print("5. Monthly Income vs Expense Bar Chart")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            plot_expense_pie()
        elif choice == '5':
            plot_monthly_bar()
        elif choice == '6':
            print("\nGoodbye! 💼💸")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")
if __name__ == "__main__":
    menu()
