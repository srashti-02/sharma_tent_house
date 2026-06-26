from services.inventory_service import (
    add_item,
    get_all_items,
    search_item,
    update_item,
    delete_item
)


def display_items(items):
    print(
        f"\n{'No.':<5}"
        f"{'ID':<12}"
        f"{'Name':<20}"
        f"{'Category':<15}"
        f"{'Qty':<8}"
        f"{'Rent':<10}"
        f"{'Status':<12}"
    )
    print("-" * 90)

    for index, item in enumerate(
        items,
        start=1
    ):
        print(
            f"{index:<5}"
            f"{item.get('item_id', 'N/A'):<12}"
            f"{item.get('item_name', 'N/A'):<20}"
            f"{item.get('category', 'N/A'):<15}"
            f"{item.get('total_quantity', 'N/A'):<8}"
            f"{item.get('standard_rent_per_day', 'N/A'):<10}"
            f"{item.get('item_status', 'N/A'):<12}"
        )


def select_item():
    name = input(
        "Enter Item Name: "
    ).strip()

    items = search_item(
        name
    )

    if not items:
        print(
            "\nNo items found."
        )
        return None

    display_items(
        items
    )

    while True:
        try:
            choice = int(
                input(
                    "\nSelect item number: "
                )
            )

            if (
                1
                <= choice
                <= len(items)
            ):
                return items[
                    choice - 1
                ]

            print(
                "Invalid selection."
            )

        except ValueError:
            print(
                "Please enter a valid number."
            )


def inventory_submenu():
    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("0. Back")

        choice = input(
            "Enter choice: "
        )

        try:
            if choice == "1":
                item_name = input(
                    "Enter Item Name: "
                ).strip()

                category = input(
                    "Enter Category: "
                ).strip()

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
                ).strip()

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

                display_items(
                    [item]
                )

            elif choice == "2":
                items = get_all_items(
                    include_inactive=True
                )

                if not items:
                    print(
                        "\nNo items found."
                    )
                else:
                    display_items(
                        items
                    )

            elif choice == "3":
                item = select_item()

                if item:
                    print(
                        "\n=== Item Details ==="
                    )

                    display_items(
                        [item]
                    )

            elif choice == "4":
                item = select_item()

                if item is None:
                    continue

                print(
                    "\nPress Enter to keep current value."
                )

                item_name = input(
                    f"Item Name "
                    f"[{item['item_name']}]: "
                ).strip()

                category = input(
                    f"Category "
                    f"[{item['category']}]: "
                ).strip()

                quantity = input(
                    f"Quantity "
                    f"[{item['total_quantity']}]: "
                ).strip()

                rent = input(
                    f"Rent Per Day "
                    f"[{item['standard_rent_per_day']}]: "
                ).strip()

                damage_charge = input(
                    f"Damage Charge "
                    f"[{item['damage_charge']}]: "
                ).strip()

                item_type = input(
                    f"Item Type "
                    f"[{item['item_type']}]: "
                ).strip()

                status = input(
                    f"Status "
                    f"[{item['item_status']}]: "
                ).strip()

                updated_item = update_item(
                    item["item_id"],
                    item_name=item_name or None,
                    category=category or None,
                    total_quantity=(
                        int(quantity)
                        if quantity
                        else None
                    ),
                    standard_rent_per_day=(
                        float(rent)
                        if rent
                        else None
                    ),
                    damage_charge=(
                        float(
                            damage_charge
                        )
                        if damage_charge
                        else None
                    ),
                    item_type=item_type or None,
                    item_status=status or None
                )

                print(
                    "\nItem updated successfully."
                )

                display_items(
                    [updated_item]
                )

            elif choice == "5":
                item = select_item()

                if item is None:
                    continue

                confirm = input(
                    f"Mark "
                    f"{item['item_name']} "
                    f"as inactive? (y/n): "
                ).lower()

                if confirm == "y":
                    deleted_item = (
                        delete_item(
                            item[
                                "item_id"
                            ]
                        )
                    )

                    print(
                        "\nItem marked inactive successfully."
                    )

                    display_items(
                        [deleted_item]
                    )

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