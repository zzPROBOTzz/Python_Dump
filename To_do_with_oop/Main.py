from fileTaskManager import FileTaskManager

def main():
    manager = FileTaskManager()

    while True:
        print("\n To-Do List")
        print("1. Add")
        print("2. Remove")
        print("3. Complete")
        print("4. List")
        print("5. Exit")

        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            manager.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            manager.remove_task(task)
        elif choice == "3":
            task = input("Enter task to mark complete: ")
            manager.complete_task(task)
        elif choice == "4":
            print("null")
        elif choice == "5":
            breakpoint()
        else:
            print("Invalid choice please select number above the numbers..")

if __name__ == "__main__":
    main()
