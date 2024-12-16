# File: inventory.py
inventory = {}

def manage_inventory():
    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Stock")
        print("2. View Stock")
        print("3. Update Stock")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_stock()
        elif choice == '2':
            view_stock()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_stock():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = inventory.get(name, 0) + quantity
    print(f"Added {quantity} of '{name}' to inventory.")

def view_stock():
    print("\n--- Inventory ---")
    for item, qty in inventory.items():
        print(f"{item}: {qty} units")

def update_stock():
    name = input("Enter item name to update: ")
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        print(f"Stock for '{name}' updated to {quantity} units.")
    else:
        print("Item not found in inventory.")
