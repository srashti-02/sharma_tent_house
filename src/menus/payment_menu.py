from services.payment_service import (
    record_deposit,
    get_payment_summary
)


def payment_menu():
    while True:
        print("\n=== Payment Menu ===")
        print("1. Record Payment")
        print("2. Payment Summary")
        print("0. Back")

        choice = input(
            "Enter choice: "
        )

        try:
            if choice == "1":
                booking_id = input(
                    "Enter Booking ID: "
                ).strip()

                amount = float(
                    input(
                        "Enter Payment Amount: ₹"
                    )
                )

                booking = record_deposit(
                    booking_id,
                    amount
                )

                print(
                    "\nPayment recorded successfully."
                )

                print(
                    f"Booking ID: "
                    f"{booking['booking_id']}"
                )

                print(
                    f"Total Paid: ₹"
                    f"{booking.get('deposit_paid', 0)}"
                )

                print(
                    f"Pending Amount: ₹"
                    f"{booking.get('pending_amount', 0)}"
                )

            elif choice == "2":
                booking_id = input(
                    "Enter Booking ID: "
                ).strip()

                summary = (
                    get_payment_summary(
                        booking_id
                    )
                )

                print(
                    "\n=== Payment Summary ==="
                )

                print(
                    f"\n{'Field':<25}"
                    f"{'Value':<25}"
                )
                print("-" * 50)

                print(
                    f"{'Booking ID':<25}"
                    f"{summary.get('booking_id', 'N/A'):<25}"
                )

                print(
                    f"{'Customer ID':<25}"
                    f"{summary.get('customer_id', 'N/A'):<25}"
                )

                print(
                    f"{'Total Amount':<25}"
                    f"₹{summary.get('final_total', 0):<24}"
                )

                print(
                    f"{'Amount Paid':<25}"
                    f"₹{summary.get('deposit_paid', 0):<24}"
                )

                print(
                    f"{'Balance Due':<25}"
                    f"₹{summary.get('balance_due', 0):<24}"
                )

                print(
                    f"{'Payment Status':<25}"
                    f"{summary.get('payment_status', 'N/A'):<25}"
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