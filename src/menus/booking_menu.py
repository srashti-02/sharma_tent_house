from services.booking_service import (
    create_booking,
    get_all_bookings,
    cancel_booking
)


def display_bookings(bookings):
    print(
        f"\n{'ID':<15}"
        f"{'Customer':<15}"
        f"{'Item':<15}"
        f"{'Qty':<8}"
        f"{'Status':<12}"
    )
    print("-" * 65)

    for booking in bookings:
        print(
            f"{booking.get('customer_id', 'N/A'):<15}"
            f"{booking.get('item_id', 'N/A'):<15}"
            f"{booking.get('quantity', 'N/A'):<8}"
            f"{booking.get('booking_status', 'N/A'):<12}"
        )


def booking_menu():
    while True:
        print("\n=== Booking Menu ===")
        print("1. Create Booking")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                customer_id = input(
                    "Enter Customer ID: "
                )
                item_id = input(
                    "Enter Item ID: "
                )
                quantity = int(
                    input(
                        "Enter Quantity: "
                    )
                )
                delivery_date = input(
                    "Enter Delivery Date (YYYY-MM-DD): "
                )
                return_date = input(
                    "Enter Return Date (YYYY-MM-DD): "
                )

                booking = create_booking(
                    customer_id,
                    item_id,
                    quantity,
                    delivery_date,
                    return_date
                )

                print(
                    "\nBooking created successfully."
                )
                print(
                    f"Booking ID: "
                    f"{booking['booking_id']}"
                )

            elif choice == "2":
                bookings = get_all_bookings()

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
                booking_id = input(
                    "Enter Booking ID: "
                )

                booking = cancel_booking(
                    booking_id
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