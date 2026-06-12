from services.inventory_service import (
add_item,
get_all_items,
search_item,
update_quantity,
update_item_status
)
from services.operations_service import (
    get_todays_deliveries,
    get_todays_collections,
    get_active_bookings,
    get_rented_inventory
)
from services.customer_service import (
    add_customer,
    get_all_customers,
    search_customer,
    get_customer_history
)
from services.booking_service import (
    create_booking,
    get_all_bookings
)

from services.availability_service import (
    check_bulk_availability
)
from services.payment_service import (
    apply_discount,
    record_deposit,
    get_payment_summary
)
from services.return_service import (
    process_return,
    record_damage,
    record_missing_items,
    calculate_settlement
)

def show_inventory_summary():
    items = get_all_items(include_inactive=True)

    total_items = len(items)

    active_items = sum(1 for item in items if item.get("item_status", "active") == "active")

    inactive_items = total_items - active_items

    total_quantity = sum(item.get("total_quantity", 0) for item in items)

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
        print("5. Mark Item Inactive")
        print("6. Inventory Summary")
        print("7. Add Customer")
        print("8. Search Customer")
        print("9. View Customers")
        print("10. Create Booking")
        print("11. Check Availability")
        print("12. View Bookings")
        print("13. View Customer History")
        print("14. Apply Discount")
        print("15. Record Deposit")
        print("16. Payment Summary")
        print("17. Today's Deliveries")
        print("18. Today's Collections")
        print("19. Active Bookings")
        print("20. Currently Rented Inventory")
        print("21. Return Booking")
        print("22. Record Damage")
        print("23. Record Missing Items")
        print("24. Settlement Summary")
        print("25. Exit")
    

        choice = input("\nEnter choice: ")

        try:
            if choice == "1":
                item_name = input("Item Name: ")
                category = input("Category: ")
                quantity = int(input("Quantity: "))
                rent = float(input("Rent Per Day: "))
                damage = float(input("Damage Charge: "))
                item_type = input("Item Type (bulk/limited/unique): ")

                item = add_item(
                    item_name,
                    category,
                    quantity,
                    rent,
                    damage,
                    item_type
                )

                print(
                    f"\nItem Added Successfully with ID "
                    f"{item['item_id']}"
                )

            elif choice == "2":
                items = get_all_items()

                if not items:
                    print("\nNo active inventory items found.")
                    continue

                print("\n===== INVENTORY =====")

                for item in items:
                    print("-" * 40)
                    print(f"ID: {item['item_id']}")
                    print(f"Name: {item['item_name']}")
                    print(f"Category: {item['category']}")
                    print(f"Quantity: {item['total_quantity']}")
                    print(
                        f"Rent/Day: Rs.{item['standard_rent_per_day']}"
                    )
                    print(
                        f"Damage Charge: Rs.{item['damage_charge']}"
                    )
                    print(f"Type: {item['item_type']}")
                    print(f"Status: {item['item_status']}")

            elif choice == "3":
                name = input("Enter item name to search: ")

                results = search_item(name)

                if not results:
                    print("\nNo item found.")
                    continue

                print("\n===== SEARCH RESULTS =====")

                for index, item in enumerate(results, start=1):
                    print("-" * 40)
                    print(f"{index}. {item['item_name']}")
                    print(f"ID: {item['item_id']}")
                    print(f"Category: {item['category']}")
                    print(f"Quantity: {item['total_quantity']}")
                    print(
                        f"Rent/Day: Rs.{item['standard_rent_per_day']}"
                    )
                    print(
                        f"Damage Charge: Rs.{item['damage_charge']}"
                    )
                    print(f"Type: {item['item_type']}")
                    print(f"Status: {item['item_status']}")

                selection = int(
                    input("\nSelect item number (0 to go back): ")
                )

                if selection == 0:
                    continue

                if selection < 1 or selection > len(results):
                    print("\nInvalid selection.")
                    continue

                selected_item = results[selection - 1]

                print("\nActions")
                print("1. Update Quantity")
                print("2. Mark Item Inactive")
                print("3. Back")

                action = input("\nChoose action: ")

                if action == "1":
                    quantity = int(input("New Quantity: "))

                    update_quantity(
                        selected_item["item_id"],
                        quantity
                    )

                    print(
                        "\nQuantity Updated Successfully"
                    )

                elif action == "2":
                    update_item_status(
                        selected_item["item_id"],
                        "inactive"
                    )

                    print(
                        "\nItem marked as inactive successfully"
                    )

            elif choice == "4":
                item_id = input("Enter Item ID: ")
                quantity = int(input("New Quantity: "))

                update_quantity(item_id, quantity)

                print("\nQuantity Updated Successfully")

            elif choice == "5":
                item_id = input("Enter Item ID: ")

                update_item_status(
                    item_id,
                    "inactive"
                )

                print(
                    "\nItem marked as inactive successfully"
                )

            elif choice == "6":
                show_inventory_summary()

            elif choice == "7":
                customer_name = input("Customer Name: ")
                phone = input("Phone: ")
                address = input("Address: ")

                customer = add_customer(
                    customer_name,
                    phone,
                    address
                )

                print(
                    f"\nCustomer Added Successfully "
                    f"with ID {customer['customer_id']}"
                )

            elif choice == "8":
                name = input(
                    "Enter customer name: "
                )

                customers = search_customer(name)

                if not customers:
                    print("\nNo customer found.")
                    continue

                print("\n===== CUSTOMERS =====")

                for customer in customers:
                    print("-" * 40)
                    print(
                        f"ID: {customer['customer_id']}"
                    )
                    print(
                        f"Name: {customer['customer_name']}"
                    )
                    print(
                        f"Phone: {customer['phone']}"
                    )
                    print(
                        f"Address: {customer['address']}"
                    )

            elif choice == "9":
                customers = get_all_customers()

                if not customers:
                    print("\nNo customers found.")
                    continue

                print("\n===== ALL CUSTOMERS =====")

                for customer in customers:
                    print("-" * 40)
                    print(
                        f"ID: {customer['customer_id']}"
                    )
                    print(
                        f"Name: {customer['customer_name']}"
                    )
                    print(
                        f"Phone: {customer['phone']}"
                    )
                    print(
                        f"Address: {customer['address']}"
                    )

            elif choice == "10":
                customer_id = input("Customer ID: ")
                item_id = input("Item ID: ")
                quantity = int(input("Quantity: "))

                delivery_date = input(
                    "Delivery Date (YYYY-MM-DD): "
                )

                return_date = input(
                    "Return Date (YYYY-MM-DD): "
                )

                booking = create_booking(
                    customer_id,
                    item_id,
                    quantity,
                    delivery_date,
                    return_date
                )

                print(
                    f"\nBooking Created: "
                    f"{booking['booking_id']}"
                )

            elif choice == "11":
                item_id = input("Item ID: ")
                quantity = int(input("Quantity: "))

                delivery_date = input(
                    "Delivery Date (YYYY-MM-DD): "
                )

                return_date = input(
                    "Return Date (YYYY-MM-DD): "
                )

                result = check_bulk_availability(
                    item_id,
                    quantity,
                    delivery_date,
                    return_date
                )

                print("\n===== AVAILABILITY =====")
                print(
                    f"Available Quantity: "
                    f"{result['available_quantity']}"
                )

                if result.get("available"):
                    print("Status: AVAILABLE")
                else:
                    print("Status: NOT AVAILABLE")

            elif choice == "12":
                bookings = get_all_bookings()

                if not bookings:
                    print("\nNo bookings found.")
                    continue

                print("\n===== BOOKINGS =====")

                for booking in bookings:
                    print("-" * 40)
                    print(
                        f"Booking ID: "
                        f"{booking['booking_id']}"
                    )
                    print(
                        f"Customer ID: "
                        f"{booking.get('customer_id', 'N/A')}"
                    )
                    print(
                        f"Item ID: "
                        f"{booking['item_id']}"
                    )
                    print(
                        f"Status: "
                        f"{booking.get('booking_status', 'active')}"
                    )
                    print(
                        f"Quantity: "
                        f"{booking['quantity']}"
                    )
                    print(
                        f"Delivery: "
                        f"{booking['delivery_date']}"
                    )
                    print(
                        f"Return: "
                        f"{booking['return_date']}"
                    )

            elif choice == "13":
                customer_id = input(
                    "Customer ID: "
                )

                bookings = get_customer_history(
                    customer_id
                )

                if not bookings:
                    print(
                        "\nNo bookings found for customer."
                    )
                    continue

                print(
                    "\n===== CUSTOMER HISTORY ====="
                )

                for booking in bookings:
                    print("-" * 40)
                    print(
                        f"Booking ID: "
                        f"{booking['booking_id']}"
                    )
                    print(
                        f"Item ID: "
                        f"{booking['item_id']}"
                    )
                    print(
                        f"Quantity: "
                        f"{booking['quantity']}"
                    )
                    print(
                        f"Delivery: "
                        f"{booking['delivery_date']}"
                    )
                    print(
                        f"Return: "
                        f"{booking['return_date']}"
                    )

            elif choice == "14":
                booking_id = input(
                    "Booking ID: "
                )

                discount = float(
                    input("Discount Amount: ")
                )

                booking = apply_discount(
                    booking_id,
                    discount
                )

                print(
                    "\nDiscount Applied Successfully"
                )

                print(
                    f"Final Total: "
                    f"{booking['final_total']}"
                )

            elif choice == "15":
                booking_id = input(
                    "Booking ID: "
                )

                amount = float(
                    input("Deposit Amount: ")
                )

                booking = record_deposit(
                    booking_id,
                    amount
                )

                print(
                    "\nDeposit Recorded Successfully"
                )

                print(
                    f"Balance Due: "
                    f"{booking['balance_due']}"
                )

            elif choice == "16":
                booking_id = input(
                    "Booking ID: "
                )

                booking = get_payment_summary(
                    booking_id
                )

                print("\n===== PAYMENT SUMMARY =====")

                print(
                    f"Booking ID: "
                    f"{booking['booking_id']}"
                )

                print(
                    f"Standard Total: "
                    f"{booking.get('standard_total', 0)}"
                )

                print(
                    f"Discount: "
                    f"{booking.get('discount', 0)}"
                )

                print(
                    f"Final Total: "
                    f"{booking.get('final_total', 0)}"
                )

                print(
                    f"Deposit Paid: "
                    f"{booking.get('deposit_paid', 0)}"
                )

                print(
                    f"Balance Due: "
                    f"{booking.get('balance_due', 0)}"
                )

                print(
                    f"Payment Status: "
                    f"{booking.get('payment_status', 'pending')}"
                )
            elif choice == "17":
                bookings = get_todays_deliveries()

                print("\n===== TODAY'S DELIVERIES =====")

                if not bookings:
                    print("No deliveries today.")
                    continue

                for booking in bookings:
                    print("-" * 40)
                    print(f"Booking: {booking['booking_id']}")
                    print(f"Customer: {booking.get('customer_id', 'N/A')}")

            elif choice == "18":
                bookings = get_todays_collections()

                print("\n===== TODAY'S COLLECTIONS =====")

                if not bookings:
                    print("No collections today.")
                    continue

                for booking in bookings:
                    print("-" * 40)
                    print(f"Booking: {booking['booking_id']}")
                    print(f"Customer: {booking.get('customer_id', 'N/A')}")

            elif choice == "19":
                bookings = get_active_bookings()

                print("\n===== ACTIVE BOOKINGS =====")

                if not bookings:
                    print("No active bookings found.")
                    continue

                for booking in bookings:
                    print("-" * 40)
                    print(f"Booking ID: {booking['booking_id']}")
                    print(f"Customer ID: {booking.get('customer_id', 'N/A')}")
                    print(f"Item ID: {booking.get('item_id', 'N/A')}")

            elif choice == "20":
                inventory = get_rented_inventory()

                print("\n===== RENTED INVENTORY =====")

                if not inventory:
                    print("No inventory currently rented.")
                    continue

                for item_id, quantity in inventory.items():
                    print(f"{item_id}: {quantity}")

            elif choice == "21":
                booking_id = input(
                    "Booking ID: "
                )

                actual_return_date = input(
                    "Actual Return Date (YYYY-MM-DD): "
                )

                booking = process_return(
                    booking_id,
                    actual_return_date
                )

                print(
                    "\nBooking Returned Successfully"
                )

                print(
                    f"Status: "
                    f"{booking['booking_status']}"
                )

            elif choice == "22":
                booking_id = input(
                    "Booking ID: "
                )

                damaged_quantity = int(
                    input("Damaged Quantity: ")
                )

                damage_fee = float(
                    input("Damage Fee: ")
                )

                record_damage(
                    booking_id,
                    damaged_quantity,
                    damage_fee
                )

                print(
                    "\nDamage Recorded Successfully"
                )

            elif choice == "23":
                booking_id = input(
                    "Booking ID: "
                )

                missing_quantity = int(
                    input("Missing Quantity: ")
                )

                replacement_fee = float(
                    input("Replacement Fee: ")
                )

                record_missing_items(
                    booking_id,
                    missing_quantity,
                    replacement_fee
                )

                print(
                    "\nMissing Items Recorded Successfully"
                )

            elif choice == "24":
                booking_id = input(
                    "Booking ID: "
                )

                booking = calculate_settlement(
                    booking_id
                )

                print(
                    "\n===== SETTLEMENT ====="
                )

                print(
                    f"Balance Due: "
                    f"{booking.get('balance_due', 0)}"
                )

                print(
                    f"Damage Fee: "
                    f"{booking.get('damage_fee', 0)}"
                )

                print(
                    f"Replacement Fee: "
                    f"{booking.get('replacement_fee', 0)}"
                )

                print(
                    f"Settlement Total: "
                    f"{booking.get('settlement_total', 0)}"
                )

            elif choice == "25":
                print("\nExiting Inventory Menu...")
                break

            else:
                print("\nInvalid choice. Please try again.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            continue

