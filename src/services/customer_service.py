from storage.json_storage import (
    load_customers,
    save_customers
)


def generate_customer_id():
    customers = load_customers()

    if not customers:
        return "CUST_001"

    max_number = 0

    for customer in customers:
        try:
            number = int(
                customer[
                    "customer_id"
                ].replace(
                    "CUST_",
                    ""
                )
            )

            max_number = max(
                max_number,
                number
            )

        except (
            KeyError,
            ValueError
        ):
            continue

    return (
        f"CUST_{max_number + 1:03d}"
    )


def add_customer(
    customer_name,
    phone,
    address
):
    customers = load_customers()

    customer = {
        "customer_id":
            generate_customer_id(),
        "customer_name":
            customer_name,
        "phone":
            phone,
        "address":
            address
    }

    customers.append(
        customer
    )

    save_customers(
        customers
    )

    return customer


def get_all_customers():
    return load_customers()


def search_customer(
    name
):
    customers = load_customers()

    return [
        customer
        for customer in customers
        if (
            name.lower()
            in customer[
                "customer_name"
            ].lower()
        )
    ]


def customer_exists(
    customer_id
):
    customers = load_customers()

    return any(
        customer.get(
            "customer_id"
        ) == customer_id
        for customer
        in customers
    )