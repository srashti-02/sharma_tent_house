from storage.json_storage import (
    load_bookings,
    save_bookings
)

from services.availability_service import (
    check_bulk_availability
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

    bookings = load_bookings()

    booking = {
        "booking_id": generate_booking_id(),
        "item_id": item_id,
        "quantity": quantity,
        "delivery_date": delivery_date,
        "return_date": return_date
    }

    bookings.append(booking)

    save_bookings(bookings)

    return booking


def get_all_bookings():
    return load_bookings()