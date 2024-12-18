def display_menu():
    print("\nGrocery List Manager")
    print("1. View List")
    print("2. Add item")
    print("3. Remove item")
    print("4. Sort list")
    print("5. Search for an item")
    print("6. Exit")

def main():
    grocery_list = []

    while True:
        display_menu()
        choice = input("Enter your choice(1-6): \n")

        if choice == "1":
            print("Your grocery list:")
            if grocery_list:
                for i, item in enumerate(grocery_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your Grocery List is empty.")


        elif choice == "2":
            item = input("Enter the item to add: ").strip()
            if item:
                grocery_list.append(item)
                print(f"'{item}'added to the list.")
            else:
                print("Item cannot be empty.")

        elif choice == "3":
            item = input("Enter an item to remove: ").strip
            if item:
                grocery_list.remove(item)
                print(f"'{item}'removed from the list.")
            else:
                print(f"'{item}'not in the list.")

        elif choice == "4":
            grocery_list.sort()
            print("Grocery List has been sorted.")

        elif choice == "5":
            item = input("Enter the name of the item to search for: ")
            if item in grocery_list:
                print(f"'{item}'is in the list.")
            else:
                print(f"'{item}'is not in the list.")

        elif choice == "6":
            print("Exiting the Grocery list.")
            break

        else:
            print("Invalid choice, Please enter a nummber between 1-6")

if __name__ == "__main__":
    main()