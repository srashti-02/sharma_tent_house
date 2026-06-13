from storage.json_storage import (
    load_bookings,
    save_bookings
)

from services.availability_service import (
    check_bulk_availability
)

from services.inventory_service import (
    get_all_items
)


def generate_booking_id():
    bookings = load_bookings()

    if not bookings:
        return "BOOKING_001"

    max_number = 0

    for booking in bookings:
        try:
            number = int(
                booking["booking_id"].replace(
                    "BOOKING_",
                    ""
                )
            )

            max_number = max(
                max_number,
                number
            )

        except (ValueError, KeyError):
            continue

    return f"BOOKING_{max_number + 1:03d}"


def create_booking(
    customer_id,
    item_id,
    quantity,
    delivery_date,
    return_date
):
    availability = check_bulk_availability(
        item_id,
        quantity,
        delivery_date,
        return_date
    )

    if not availability["available"]:
        raise ValueError(
            f"Not enough inventory available. "
            f"Only {availability['available_quantity']} left."
        )

    inventory_items = get_all_items()

    rent = None

    for item in inventory_items:
        if item["item_id"] == item_id:
            rent = item["standard_rent_per_day"]
            break

    if rent is None:
        raise ValueError("Item not found.")

    standard_total = rent * quantity

    bookings = load_bookings()

    booking = {
        "booking_id": generate_booking_id(),
        "customer_id": customer_id,
        "item_id": item_id,
        "quantity": quantity,
        "delivery_date": delivery_date,
        "return_date": return_date,
        "booking_status": "active",

        # Phase 3C
        "standard_total": standard_total,
        "discount": 0,
        "final_total": standard_total,
        "deposit_paid": 0,
    }

    bookings.append(booking)

    save_bookings(bookings)

    return booking


def get_all_bookings():
    return load_bookings()


def get_customer_bookings(customer_id):
    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("customer_id") == customer_id
    ]


def cancel_booking(booking_id):
    bookings = load_bookings()

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            booking["booking_status"] = "cancelled"

            save_bookings(bookings)

            return booking

    raise ValueError("Booking not found.")