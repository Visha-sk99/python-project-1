import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
def init_csv():
    if not os.path.exists("students.csv"):
        df = pd.DataFrame(columns=["Name", "Roll No", "Math", "Science", "English"])
        df.to_csv("students.csv", index=False)
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    
    new_data = pd.DataFrame([[name, roll, math, science, english]],
                            columns=["Name", "Roll No", "Math", "Science", "English"])
    
    new_data.to_csv("students.csv", mode='a', index=False, header=False)
    print("\n✅ Student added successfully!\n")
def view_students():
    df = pd.read_csv("students.csv")
    print("\n--- Student Records ---\n")
    print(df)
def calculate_analytics():
    df = pd.read_csv("students.csv")
    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

    topper = df.loc[df["Average"].idxmax()]
    
    print("\n📊 Class Average:\n")
    print(df[["Name", "Roll No", "Average"]])

    print("\n🏆 Topper of the Class:")
    print(topper[["Name", "Roll No", "Average"]])
def plot_performance():
    df = pd.read_csv("students.csv")
    df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

    plt.figure(figsize=(10,6))
    plt.bar(df["Name"], df["Average"], color='skyblue')
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("📈 Student Performance Chart")
    plt.grid(True)
    plt.show()
def menu():
    init_csv()
    while True:
        print("\n========= STUDENT MANAGEMENT SYSTEM =========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Analytics")
        print("4. Show Performance Chart")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            calculate_analytics()
        elif choice == '4':
            plot_performance()
        elif choice == '5':
            print("\nExiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    menu()
