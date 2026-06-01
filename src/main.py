# from services.inventory_service import get_all_items

# items = get_all_items()

# print("\n===== INVENTORY =====\n")

# for item in items:
#     print(f"ID: {item['item_id']}")
#     print(f"Name: {item['item_name']}")
#     print(f"Category: {item['category']}")
#     print(f"Quantity: {item['total_quantity']}")
#     print(f"Rent/Day: ₹{item['standard_rent_per_day']}")
#     print(f"Damage Charge: ₹{item['damage_charge']}")
#     print(f"Type: {item['item_type']}")
#     print(f"Status: {item['item_status']}")
#     print("-" * 40)

from menus.inventory_menu import inventory_menu

inventory_menu()
