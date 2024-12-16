# File: report.py
import order

def view_sales_report():
    print("\n--- Sales Report ---")
    total_sales = sum(o['total'] for o in order.orders)
    print(f"Total Orders: {len(order.orders)}")
    print(f"Total Sales: ${total_sales:.2f}")
