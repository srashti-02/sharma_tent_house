from services.inventory_service import (
    add_item,
    get_all_items,
    search_item,
    update_quantity,
    update_item_status
)


def display_items(items):
    print(
        f"\n{'ID':<12}"
        f"{'Name':<20}"
        f"{'Category':<15}"
        f"{'Qty':<8}"
        f"{'Rent':<10}"
        f"{'Status':<12}"
    )
    print("-" * 77)

    for item in items:
        print(
            f"{item.get('item_id', 'N/A'):<12}"
            f"{item.get('item_name', 'N/A'):<20}"
            f"{item.get('category', 'N/A'):<15}"
            f"{item.get('total_quantity', 'N/A'):<8}"
            f"{item.get('standard_rent_per_day', 'N/A'):<10}"
            f"{item.get('item_status', 'N/A'):<12}"
        )


def inventory_submenu():
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Update Quantity")
        print("5. Mark Item Inactive")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                item_name = input(
                    "Enter Item Name: "
                )
                category = input(
                    "Enter Category: "
                )
                total_quantity = int(
                    input(
                        "Enter Quantity: "
                    )
                )
                standard_rent_per_day = float(
                    input(
                        "Enter Rent Per Day: "
                    )
                )
                damage_charge = float(
                    input(
                        "Enter Damage Charge: "
                    )
                )
                item_type = input(
                    "Enter Item Type: "
                )

                item = add_item(
                    item_name,
                    category,
                    total_quantity,
                    standard_rent_per_day,
                    damage_charge,
                    item_type
                )

                print(
                    "\nItem added successfully."
                )
                print(
                    f"Item ID: "
                    f"{item['item_id']}"
                )

            elif choice == "2":
                items = get_all_items()

                if not items:
                    print(
                        "\nNo items found."
                    )
                else:
                    print(
                        "\n=== Inventory Items ==="
                    )
                    display_items(items)

            elif choice == "3":
                name = input(
                    "Enter Item Name: "
                )

                items = search_item(name)

                if not items:
                    print(
                        "\nNo items found."
                    )
                else:
                    display_items(items)

            elif choice == "4":
                item_id = input(
                    "Enter Item ID: "
                )
                quantity = int(
                    input(
                        "Enter New Quantity: "
                    )
                )

                item = update_quantity(
                    item_id,
                    quantity
                )

                print(
                    "\nQuantity updated successfully."
                )
                print(item)

            elif choice == "5":
                item_id = input(
                    "Enter Item ID: "
                )

                item = update_item_status(
                    item_id,
                    "inactive"
                )

                print(
                    "\nItem marked inactive."
                )
                print(item)

            elif choice == "0":
                break

            else:
                print(
                    "Invalid choice."
                )

        except Exception as error:
            print(
                f"Error: {error}"
            )