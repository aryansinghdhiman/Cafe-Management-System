# File: order.py
import menu

orders = []

def take_order():
    print("\n--- Take Order ---")
    if not menu.menu_items:
        print("Menu is empty. Please add items first.")
        return
    
    menu.view_menu()
    order_items = []
    while True:
        item_num = input("Enter item number to add to order (or 'done' to finish): ")
        if item_num.lower() == 'done':
            break
        try:
            item_num = int(item_num) - 1
            if 0 <= item_num < len(menu.menu_items):
                order_items.append(menu.menu_items[item_num])
            else:
                print("Invalid item number. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    total = sum(item['price'] for item in order_items)
    print("\nOrder Summary:")
    for item in order_items:
        print(f"- {item['name']} - ${item['price']:.2f}")
    print(f"Total: ${total:.2f}")
    orders.append({"items": order_items, "total": total})
