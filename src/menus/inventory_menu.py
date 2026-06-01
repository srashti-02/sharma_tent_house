from services.inventory_service import add_item, get_all_items, search_item, update_quantity

def show_inventory_summary():
    items = get_all_items()

    total_items = len(items)
    active_items = sum(
        1
        for item in items
        if item.get("item_status", "active") == "active"
    )
    inactive_items = total_items - active_items
    total_quantity = sum(
        item.get("total_quantity", 0)
        for item in items
    )

    categories = {}
    for item in items:
        category = item.get("category", "Unknown")
        categories[category] = categories.get(category, 0) + 1

    print("\n===== INVENTORY SUMMARY =====")
    print(f"Total Items: {total_items}")
    print(f"Active Items: {active_items}")
    print(f"Inactive Items: {inactive_items}")
    print(f"Total Quantity: {total_quantity}")

    print("\nCategories:")
    for category, count in categories.items():
        print(f"- {category}: {count}")


def inventory_menu():
    while True:
        print("\n" + "=" * 40)
        print("     SHARMA TENT HOUSE")
        print("=" * 40)
        print("1. Add Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Update Quantity")
        print("5. Inventory Summary")
        print("6. Exit")

        choice = input("\nEnter choice: ")

        try:
            if choice == "1":
                item_id = input("Item ID: ")
                item_name = input("Item Name: ")
                category = input("Category: ")
                quantity = int(input("Quantity: "))
                rent = float(input("Rent Per Day: "))
                damage = float(input("Damage Charge: "))
                item_type = input("Item Type (bulk/limited/unique): ")

                add_item(
                    item_id,
                    item_name,
                    category,
                    quantity,
                    rent,
                    damage,
                    item_type,
                )

                print("\nItem Added Successfully")

            elif choice == "2":
                items = get_all_items()

                if not items:
                    print("\nNo inventory items found.")
                    continue

                print("\n===== INVENTORY =====")
                for item in items:
                    print("-" * 40)
                    print(f"ID: {item['item_id']}")
                    print(f"Name: {item['item_name']}")
                    print(f"Category: {item['category']}")
                    print(f"Quantity: {item['total_quantity']}")
                    print(f"Rent/Day: Rs.{item['standard_rent_per_day']}")
                    print(f"Damage Charge: Rs.{item['damage_charge']}")
                    print(f"Type: {item['item_type']}")
                    print(f"Status: {item['item_status']}")

            elif choice == "3":
                name = input("Enter item name to search: ")

                results = search_item(name)

                if not results:
                    print("\nNo item found.")
                    continue

                print("\n===== SEARCH RESULTS =====")
                for item in results:
                    print("-" * 40)
                    print(f"ID: {item['item_id']}")
                    print(f"Name: {item['item_name']}")
                    print(f"Quantity: {item['total_quantity']}")

            elif choice == "4":
                item_id = input("Enter Item ID: ")
                quantity = int(input("New Quantity: "))

                update_quantity(item_id, quantity)

                print("\nQuantity Updated Successfully")

            elif choice == "5":
                show_inventory_summary()

            elif choice == "6":
                print("\nThank you for using Sharma Tent House System.")
                break

            else:
                print("\nInvalid option.")

        except ValueError as error:
            print(f"\nError: {error}")

