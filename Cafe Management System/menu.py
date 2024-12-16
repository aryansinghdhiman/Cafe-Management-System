# File: menu.py
menu_items = []

def manage_menu():
    while True:
        print("\n--- Menu Management ---")
        print("1. Add Item")
        print("2. View Menu")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_menu()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    menu_items.append({"name": name, "price": price})
    print(f"Item '{name}' added successfully!")

def view_menu():
    print("\n--- Menu ---")
    for i, item in enumerate(menu_items, start=1):
        print(f"{i}. {item['name']} - ${item['price']:.2f}")

def update_item():
    view_menu()
    index = int(input("Enter the item number to update: ")) - 1
    if 0 <= index < len(menu_items):
        name = input("Enter new name: ")
        price = float(input("Enter new price: "))
        menu_items[index] = {"name": name, "price": price}
        print("Item updated successfully!")
    else:
        print("Invalid item number.")

def delete_item():
    view_menu()
    index = int(input("Enter the item number to delete: ")) - 1
    if 0 <= index < len(menu_items):
        removed_item = menu_items.pop(index)
        print(f"Item '{removed_item['name']}' deleted successfully!")
    else:
        print("Invalid item number.")

if __name__ == "__main__":
    manage_menu()
