from services.customer_service import (
    search_customer,
    add_customer,
    get_customer_by_id
)

from services.booking_service import (
    create_booking,
    get_all_bookings,
    get_customer_bookings,
    cancel_booking
)

from services.inventory_service import (
    get_all_items
)

def search_bookings_by_customer():
    name = input(
        "Enter Customer Name: "
    ).strip()

    customers = search_customer(
        name
    )

    if not customers:
        print(
            "\nCustomer not found."
        )

        choice = input(
            "Create new customer? (y/n): "
        ).lower()

        if choice != "y":
            return None

        customer_name = input(
            "Enter Customer Name: "
        ).strip()

        phone = input(
            "Enter Phone Number: "
        ).strip()

        address = input(
            "Enter Address: "
        ).strip()

        customer = add_customer(
            customer_name,
            phone,
            address
        )

        print(
            "\nCustomer created successfully."
        )
        return customer[
            "customer_id"
        ]

    print(
        "\n=== Matching Customers ==="
    )

    print(
        f"\n{'No.':<5}"
        f"{'ID':<15}"
        f"{'Name':<25}"
        f"{'Phone':<15}"
    )
    print("-" * 60)

    for index, customer in enumerate(
        customers,
        start=1
    ):
        print(
            f"{index:<5}"
            f"{customer['customer_id']:<15}"
            f"{customer['customer_name']:<25}"
            f"{customer['phone']:<15}"
        )

    try:
        choice = int(
            input(
                "\nSelect customer number: "
            )
        )

        if not (
            1
            <= choice
            <= len(customers)
        ):
            print(
                "Invalid selection."
            )
            return

        customer_id = customers[
            choice - 1
        ][
            "customer_id"
        ]

        bookings = (
            get_customer_bookings(
                customer_id
            )
        )

        if not bookings:
            print(
                "\nNo bookings found for this customer."
            )
            return

        print(
            f"\n=== Bookings for "
            f"{customers[choice - 1]['customer_name']} ==="
        )

        display_bookings(
            bookings
        )

    except ValueError:
        print(
            "Please enter a valid number."
        )

def select_item():
    name = input(
        "Enter Item Name: "
    ).strip()

    items = [
        item
        for item in get_all_items()
        if (
            name.lower()
            in item[
                "item_name"
            ].lower()
        )
    ]

    if not items:
        print(
            "\nNo matching items found."
        )
        return None

    print(
        "\n=== Available Items ==="
    )

    print(
        f"\n{'No.':<5}"
        f"{'ID':<15}"
        f"{'Name':<25}"
        f"{'Available':<12}"
        f"{'Rent':<10}"
    )
    print("-" * 75)

    for index, item in enumerate(
        items,
        start=1
    ):
        print(
            f"{index:<5}"
            f"{item['item_id']:<15}"
            f"{item['item_name']:<25}"
            f"{item['total_quantity']:<12}"
            f"{item['standard_rent_per_day']:<10}"
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


def display_bookings(bookings):
    print(
        f"\n{'Booking ID':<15}"
        f"{'Customer':<15}"
        f"{'Date':<15}"
        f"{'Total':<12}"
        f"{'Deposit':<12}"
        f"{'Pending':<12}"
        f"{'Status':<12}"
    )
    print("-" * 95)

    for booking in bookings:
        print(
            f"{booking.get('booking_id', 'N/A'):<15}"
            f"{booking.get('customer_id', 'N/A'):<15}"
            f"{booking.get('booking_date', 'N/A'):<15}"
            f"{booking.get('standard_total', 0):<12}"
            f"{booking.get('deposit_paid', 0):<12}"
            f"{booking.get('pending_amount', 0):<12}"
            f"{booking.get('booking_status', 'N/A'):<12}"
        )


def select_customer():
    name = input(
        "Enter Customer Name: "
    ).strip()

    customers = search_customer(
        name
    )

    if not customers:
        print(
            "\nCustomer not found."
        )

        choice = input(
            "Create new customer? (y/n): "
        ).lower()

        if choice != "y":
            return None

        customer_name = input(
            "Enter Customer Name: "
        ).strip()

        phone = input(
            "Enter Phone Number: "
        ).strip()

        address = input(
            "Enter Address: "
        ).strip()

        customer = add_customer(
            customer_name,
            phone,
            address
        )

        print(
            "\nCustomer created successfully."
        )
        print(
            f"Customer ID: "
            f"{customer['customer_id']}"
        )

        return customer[
            "customer_id"
        ]

    print(
        "\n=== Matching Customers ==="
    )

    print(
        f"\n{'No.':<5}"
        f"{'ID':<15}"
        f"{'Name':<25}"
        f"{'Phone':<15}"
    )
    print("-" * 60)

    for index, customer in enumerate(
        customers,
        start=1
    ):
        print(
            f"{index:<5}"
            f"{customer['customer_id']:<15}"
            f"{customer['customer_name']:<25}"
            f"{customer['phone']:<15}"
        )

    print("\n1. Select Existing Customer")
    print("2. Create New Customer")

    option = input(
        "Enter choice: "
    ).strip()

    if option == "1":
        while True:
            try:
                choice = int(
                    input(
                        "\nSelect customer number: "
                    )
                )

                if (
                    1
                    <= choice
                    <= len(customers)
                ):
                    return customers[
                        choice - 1
                    ]["customer_id"]

                print(
                    "Invalid selection."
                )

            except ValueError:
                print(
                    "Please enter a valid number."
                )

    elif option == "2":
        customer_name = input(
            "Enter Customer Name: "
        ).strip()

        phone = input(
            "Enter Phone Number: "
        ).strip()

        address = input(
            "Enter Address: "
        ).strip()

        customer = add_customer(
            customer_name,
            phone,
            address
        )

        print(
            "\nCustomer created successfully."
        )
        print(
            f"Customer ID: "
            f"{customer['customer_id']}"
        )

        return customer[
            "customer_id"
        ]

    return None


def booking_menu():
    while True:
        print("\n=== Booking Menu ===")
        print("1. Create Booking")
        print("2. View Bookings")
        print("3. Search Bookings by Customer")
        print("4. Cancel Booking")
        print("0. Back")

        choice = input(
            "Enter choice: "
        )

        try:
            if choice == "1":
                customer_id = (
                    select_customer()
                )

                if customer_id is None:
                    continue

                selected_items = []
                total_charge = 0

                while True:
                    item = select_item()

                    if item is None:
                        break

                    quantity = int(
                        input(
                            "Enter Quantity: "
                        )
                    )

                    item_total = (
                        item[
                            "standard_rent_per_day"
                        ]
                        * quantity
                    )

                    selected_items.append(
                        {
                            "item_id":
                                item[
                                    "item_id"
                                ],
                            "item_name":
                                item[
                                    "item_name"
                                ],
                            "quantity":
                                quantity,
                            "total":
                                item_total
                        }
                    )

                    total_charge += (
                        item_total
                    )

                    add_more = input(
                        "Add another item? (y/n): "
                    ).lower()

                    if add_more != "y":
                        break

                if not selected_items:
                    print(
                        "\nNo items selected."
                    )
                    continue

                if len(selected_items) > 1:
                    print(
                        "\nCurrently only one item per booking "
                        "is supported."
                    )
                    continue

                booking_date = input(
                    "Enter Booking Date "
                    "(YYYY-MM-DD): "
                ).strip()

                booking_time = input(
                    "Enter Booking Time "
                    "(HH:MM): "
                ).strip()

                delivery_date = input(
                    "Enter Delivery Date "
                    "(YYYY-MM-DD): "
                ).strip()

                return_date = input(
                    "Enter Return Date "
                    "(YYYY-MM-DD): "
                ).strip()

                return_time = input(
                    "Enter Return Time "
                    "(HH:MM): "
                ).strip()

                print(
                    f"\nTotal Charge: ₹{total_charge}"
                )
                print(
                    "\n=== Selected Items ==="
                )

                print(
                    f"\n{'Item':<25}"
                    f"{'Qty':<10}"
                    f"{'Amount':<10}"
                )
                print("-" * 45)

                for item in selected_items:      
                    print(
                     f"{item['item_name']:<25}"
                     f"{item['quantity']:<10}"
                     f"₹{item['total']:<10}"
                    )

                print(
                    f"\nTotal Charge: "
                    f"₹{total_charge}"
                )

                minimum_deposit = (
                    total_charge * 0.20
                )
                print(
                    f"Minimum Deposit Required: "
                    f"₹{minimum_deposit:.0f}"
                )

                while True:
                    try:
                        deposit_paid = float(
                            input(
                                "Enter Deposit Amount: ₹"
                            )
                        )

                        if deposit_paid <= 0:
                            print(
                                "Deposit amount must be greater than 0."
                            )
                            continue

                        if deposit_paid < minimum_deposit:
                            print(
                                f"Deposit amount must be at least ₹{minimum_deposit:.0f}."
                            )
                            continue

                        break

                    except ValueError:
                        print(
                            "Please enter a valid amount."
                        )

                item_id = selected_items[0]["item_id"]
                quantity = selected_items[0]["quantity"]

                booking = create_booking(
                    customer_id,
                    item_id,
                    quantity,
                    booking_date,
                    booking_time,
                    delivery_date,
                    return_date,
                    return_time,
                    deposit_paid
                )

                print(
                    "\nBooking confirmed successfully."
                )
                print(
                    f"Deposit Paid: "
                    f"₹{booking['deposit_paid']}"
                )
                print(
                    f"Pending Amount: "
                    f"₹{booking['pending_amount']}"
                )
                print(
                    "\n=== Booking Details ==="
                )

                display_bookings(
                    [booking]
                )

            elif choice == "2":
                bookings = (
                    get_all_bookings()
                )

                if not bookings:
                    print(
                        "\nNo bookings found."
                    )
                else:
                    print(
                        "\n=== All Bookings ==="
                    )
                    display_bookings(
                        bookings
                   )
            
            elif choice == "3":
                search_bookings_by_customer()
                    
            elif choice == "4":
                booking_id = input(
                    "Enter Booking ID: "
                )

                booking = (
                    cancel_booking(
                        booking_id
                    )
                )

                print(
                    "\nBooking cancelled successfully."
                )
                print(
                    f"Booking ID: "
                    f"{booking['booking_id']}"
                )
                print(
                    f"Refund Amount: "
                    f"{booking.get('refund_amount', 0)}"
                )

            elif choice == "0":
                break

            else:
                print(
                    "Invalid choice."
                )

        except ValueError as error:
            print(
                f"Error: {error}"
            )
