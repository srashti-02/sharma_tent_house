from services.report_service import (
    revenue_report,
    damage_report,
    missing_inventory_report,
    returned_booking_report,
    inventory_utilization_report
)


def report_menu():
    while True:
        print("\n=== Report Menu ===")
        print("1. Revenue Report")
        print("2. Damage Report")
        print("3. Missing Inventory Report")
        print("4. Returned Booking Report")
        print("5. Inventory Utilization Report")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                report = revenue_report()

                print("\n=== Revenue Report ===")
                print("-" * 35)
                print(
                    f"Total Revenue      : "
                    f"{report['total_revenue']}"
                )
                print(
                    f"Total Deposits     : "
                    f"{report['total_deposits']}"
                )
                print(
                    f"Outstanding Balance: "
                    f"{report['outstanding_balance']}"
                )

            elif choice == "2":
                reports = damage_report()

                print("\n=== Damage Report ===")

                if not reports:
                    print(
                        "No damaged items found."
                    )
                else:
                    for booking in reports:
                        print(
                            f"Booking ID : "
                            f"{booking['booking_id']}"
                        )
                        print(
                            f"Damage Fee : "
                            f"{booking.get('damage_fee', 0)}"
                        )
                        print("-" * 35)

            elif choice == "3":
                reports = (
                    missing_inventory_report()
                )

                print(
                    "\n=== Missing Inventory Report ==="
                )

                if not reports:
                    print(
                        "No missing items found."
                    )
                else:
                    for booking in reports:
                        print(
                            f"Booking ID      : "
                            f"{booking['booking_id']}"
                        )
                        print(
                            f"Replacement Fee : "
                            f"{booking.get('replacement_fee', 0)}"
                        )
                        print("-" * 35)

            elif choice == "4":
                report = (
                    returned_booking_report()
                )

                print(
                    "\n=== Returned Booking Report ==="
                )
                print("-" * 35)
                print(
                    f"Total Returned   : "
                    f"{report['total_returned']}"
                )
                print(
                    f"Settlement Total : "
                    f"{report['total_settlement']}"
                )

            elif choice == "5":
                report = (
                    inventory_utilization_report()
                )

                print(
                    "\n=== Inventory Utilization Report ==="
                )

                if not report:
                    print(
                        "No active bookings found."
                    )
                else:
                    print(
                        f"Most Rented Item  : "
                        f"{report['most_rented']}"
                    )
                    print(
                        f"Least Rented Item : "
                        f"{report['least_rented']}"
                    )

                    print(
                        "\nRented Quantities:"
                    )

                    for (
                        item_id,
                        quantity
                    ) in report[
                        "rented_quantities"
                    ].items():
                        print(
                            f"{item_id}: "
                            f"{quantity}"
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