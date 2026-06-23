from menus.inventory_submenu import (
    inventory_submenu
)
from menus.customer_menu import (
    customer_menu
)
from menus.booking_menu import (
    booking_menu
)
from menus.payment_menu import (
    payment_menu
)
from menus.return_menu import (
    return_menu
)
from menus.report_menu import (
    report_menu
)


def inventory_menu():
    while True:
        print("\n===== SHARMA TENT HOUSE =====")
        print("1. Inventory")
        print("2. Customers")
        print("3. Bookings")
        print("4. Payments")
        print("5. Returns")
        print("6. Reports")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory_submenu()

        elif choice == "2":
            customer_menu()

        elif choice == "3":
            booking_menu()

        elif choice == "4":
            payment_menu()

        elif choice == "5":
            return_menu()

        elif choice == "6":
            report_menu()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")