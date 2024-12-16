# File: cafe_management_system.py
import menu
import order
import inventory
import report

def main():
    while True:
        print("\n--- Cafe Management System ---")
        print("1. Manage Menu")
        print("2. Take Order")
        print("3. Manage Inventory")
        print("4. View Sales Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            menu.manage_menu()
        elif choice == '2':
            order.take_order()
        elif choice == '3':
            inventory.manage_inventory()
        elif choice == '4':
            report.view_sales_report()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
