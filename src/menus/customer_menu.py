from services.customer_service import (
    add_customer,
    search_customer,
    get_all_customers
)


def display_customers(customers):
    print(
        f"\n{'ID':<12}"
        f"{'Name':<25}"
        f"{'Phone':<15}"
        f"{'Address':<20}"
    )
    print("-" * 72)

    for customer in customers:
        print(
            f"{customer['customer_id']:<12}"
            f"{customer['customer_name']:<25}"
            f"{customer['phone']:<15}"
            f"{customer['address']:<20}"
        )


def customer_menu():
    while True:
        print("\n=== Customer Menu ===")
        print("1. Add Customer")
        print("2. Search Customer")
        print("3. View Customers")
        print("0. Back")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                customer_name = input(
                    "Enter Customer Name: "
                )
                phone = input(
                    "Enter Phone Number: "
                )
                address = input(
                    "Enter Address: "
                )

                customer = add_customer(
                    customer_name,
                    phone,
                    address
                )

                print(
                    "\nCustomer added successfully."
                )
                print(
                    f"Customer ID: "
                    f"{customer['customer_id']}"
                )

            elif choice == "2":
                name = input(
                    "Enter Customer Name: "
                )

                customers = search_customer(
                    name
                )

                if not customers:
                    print(
                        "\nNo customer found."
                    )
                else:
                    print(
                        "\n=== Search Results ==="
                    )
                    display_customers(
                        customers
                    )

            elif choice == "3":
                customers = (
                    get_all_customers()
                )

                if not customers:
                    print(
                        "\nNo customers found."
                    )
                else:
                    print(
                        "\n=== All Customers ==="
                    )
                    display_customers(
                        customers
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