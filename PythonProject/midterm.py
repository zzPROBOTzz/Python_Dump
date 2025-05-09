#Meet Hingu
# Midterm Exam

def options():
    print("\nWelcome to my shopping mart.")
    print("1.Add items in the shopping list.")
    print("2.Remove items in the shopping list.")
    print("3.view all items in the shopping list.")
    print("4.check if the items is in the shopping list.")
    print("5. Quit")

# this is for add item to shopping list
def add_item(shopping_list):
    item = input("How many Items you want to add:").strip()
   # add = int(input("Added item in quantity:"))
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")

    else:
        print("Add something in the list.")

# this is for removing item from shopping List
def remove_item(shopping_list):
    item = input("what items you want to remove:")
    #remove = int(input("How many of that you want to remove: "))
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"this {item} is remove from the bill")
    else:
        print("This item is not in the list.")

# view all the item
def view_all_items(shopping_list):
    if not shopping_list:
        print("Its not in shopping list.")
    else:
        for index,item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

# check if this is in the list or not
def check_items(shopping_list):
    item = input("plaese write the item in the list that you want to check:")
    if not shopping_list:
        print("Its not in shopping list.")
    else:
        print(f"{item} is in the list.")





shopping_list = []
while True:
    options()
    choice = input("Enter the option that are given (1 - 5):")

    if choice == '1':
        add_item(shopping_list)
    elif choice == '2':
        remove_item(shopping_list)
    elif choice == '3':
        view_all_items(shopping_list)
    elif choice == '4':
        check_items(shopping_list)
    elif choice == '5':
       print("Thank you for shopping! Good Bye!")
       break
    else:
       print("Invalid option")


