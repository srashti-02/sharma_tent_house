from services.payment_service import (
    record_deposit,
    get_payment_summary
)


def payment_menu():
    while True:
        print("\n=== Payment Menu ===")
        print("1. Record Deposit")
        print("2. Payment Summary")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                booking_id = input(
                    "Enter Booking ID: "
                )

                deposit_amount = float(
                    input(
                        "Enter Deposit Amount: "
                    )
                )

                booking = record_deposit(
                    booking_id,
                    deposit_amount
                )

                print(
                    "\nDeposit recorded successfully."
                )
                print(
                    f"Booking ID: "
                    f"{booking['booking_id']}"
                )
                print(
                    f"Deposit Paid: "
                    f"{booking.get('deposit_paid', 0)}"
                )

            elif choice == "2":
                booking_id = input(
                    "Enter Booking ID: "
                )

                summary = get_payment_summary(
                    booking_id
                )

                print(
                    "\n=== Payment Summary ==="
                )

                for key, value in summary.items():
                    print(
                        f"{key}: {value}"
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