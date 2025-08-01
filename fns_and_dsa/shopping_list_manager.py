def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice_input = input("Enter your choice: ")
        if not choice_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice = int(choice_input)

        if choice == 1:
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        elif choice == 2:
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
