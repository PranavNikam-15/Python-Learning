def todo_app():
    
    tasks = []
    while True:

        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == '2':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == '3':

            try:
                idx = int(input("Enter task number to delete: "))

                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Choose between 1 and 4.")

todo_app()