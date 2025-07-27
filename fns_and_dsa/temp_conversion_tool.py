# Define global conversion factors (for temperature conversion as an example)
CONVERSIONS = {
    'C_to_F': lambda c: (c * 9/5) + 32,
    'F_to_C': lambda f: (f - 32) * 5/9,
    'C_to_K': lambda c: c + 273.15,
    'K_to_C': lambda k: k - 273.15
}

def display_menu(): 
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Temperature conversion")
    print("5. Exit")

def temperature_conversion():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    try:
        choice = int(input("Choose a conversion (1-4): "))
        temp = float(input("Enter the temperature to convert: "))
        
        if choice == 1:
            result = CONVERSIONS['C_to_F'](temp)
            print(f"{temp} Celsius is {result} Fahrenheit.")
        elif choice == 2:
            result = CONVERSIONS['F_to_C'](temp)
            print(f"{temp} Fahrenheit is {result} Celsius.")
        elif choice == 3:
            result = CONVERSIONS['C_to_K'](temp)
            print(f"{temp} Celsius is {result} Kelvin.")
        elif choice == 4:
            result = CONVERSIONS['K_to_C'](temp)
            print(f"{temp} Kelvin is {result} Celsius.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    shopping_list = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
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
                temperature_conversion()  # Call temperature conversion
            elif choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
