from services.return_service import (
    process_return,
    record_damage,
    record_missing_items,
    calculate_late_fee,
    calculate_settlement
)


def display_booking(booking):
    print("\n" + "-" * 70)
    print(
        f"{'Field':<25}"
        f"{'Value'}"
    )
    print("-" * 70)

    for key, value in booking.items():
        label = (
            key.replace(
                "_",
                " "
            ).title()
        )

        print(
            f"{label:<25}"
            f"{value}"
        )

    print("-" * 70)


def return_menu():
    while True:
        print("\n=== Return Menu ===")
        print("1. Process Return")
        print("2. Record Damage")
        print("3. Record Missing Items")
        print("4. Calculate Late Fee")
        print("5. Calculate Settlement")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                booking_id = input(
                    "Enter Booking ID: "
                )
                actual_return_date = input(
                    "Enter Actual Return Date (YYYY-MM-DD): "
                )

                booking = process_return(
                    booking_id,
                    actual_return_date
                )

                print(
                    "\nReturn processed successfully."
                )
                display_booking(
                    booking
                )

            elif choice == "2":
                booking_id = input(
                    "Enter Booking ID: "
                )
                damaged_quantity = int(
                    input(
                        "Enter Damaged Quantity: "
                    )
                )
                damage_fee = float(
                    input(
                        "Enter Damage Fee: "
                    )
                )

                booking = record_damage(
                    booking_id,
                    damaged_quantity,
                    damage_fee
                )

                print(
                    "\nDamage recorded successfully."
                )
                display_booking(
                    booking
                )

            elif choice == "3":
                booking_id = input(
                    "Enter Booking ID: "
                )
                missing_quantity = int(
                    input(
                        "Enter Missing Quantity: "
                    )
                )
                replacement_fee = float(
                    input(
                        "Enter Replacement Fee: "
                    )
                )

                booking = record_missing_items(
                    booking_id,
                    missing_quantity,
                    replacement_fee
                )

                print(
                    "\nMissing items recorded successfully."
                )
                display_booking(
                    booking
                )

            elif choice == "4":
                booking_id = input(
                    "Enter Booking ID: "
                )

                booking = calculate_late_fee(
                    booking_id
                )

                print(
                    "\nLate fee calculated successfully."
                )
                display_booking(
                    booking
                )

            elif choice == "5":
                booking_id = input(
                    "Enter Booking ID: "
                )

                booking = calculate_settlement(
                    booking_id
                )

                print(
                    "\nSettlement calculated successfully."
                )
                display_booking(
                    booking
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