"""
Simple command-line to-do list.
Built to practice lists, loops, functions, and user input.
"""

tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "4":
        print("Goodbye!")
        break
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {tasks}")
    else:
        print("Option not implemented yet.")
