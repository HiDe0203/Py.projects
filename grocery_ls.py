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
        choice = input("Enter your choice(1-6): ")

        if choice == "1":
            print("Your grocery list:")
            if grocery_list:
                for i, item in enumerate(grocery_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your Grocery List is empty.")


        if choice == "2":
            item = input("Enter the item to add: ").strip()
            if item:
                grocery_list.append(item)
                print(f"'{item}'added to the list.")
            else:
                print("Item cannot be empty.")

        if choice == "3":
            item = input("Enter an item to remove: ").strip
            if item:
                grocery_list.remove(item)
                print(f"'{item}'removed from the list.")