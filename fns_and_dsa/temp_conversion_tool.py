def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                # Removed trailing space from prompt
                item = input("Enter the item to add:")  
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            elif choice == 2:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            elif choice == 3:
                index = int(input("Enter the item number to remove: "))
                if 1 <= index <= len(shopping_list):
                    removed = shopping_list.pop(index - 1)
                    print(f"Removed '{removed}' from the shopping list.")
                else:
                    print("Invalid item number.")
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
