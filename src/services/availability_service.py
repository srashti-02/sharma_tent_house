from datetime import datetime

from storage.json_storage import (
    load_inventory,
    load_bookings
)


def dates_overlap(
    existing_start,
    existing_end,
    requested_start,
    requested_end
):
    existing_start = datetime.strptime(
        existing_start,
        "%Y-%m-%d"
    )

    existing_end = datetime.strptime(
        existing_end,
        "%Y-%m-%d"
    )

    requested_start = datetime.strptime(
        requested_start,
        "%Y-%m-%d"
    )

    requested_end = datetime.strptime(
        requested_end,
        "%Y-%m-%d"
    )

    return not (
        existing_end < requested_start
        or
        existing_start > requested_end
    )


def get_item_by_id(item_id):
    inventory = load_inventory()

    for item in inventory:
        if item["item_id"] == item_id:
            return item

    return None


def calculate_booked_quantity(
    item_id,
    delivery_date,
    return_date
):
    bookings = load_bookings()

    booked_quantity = 0

    for booking in bookings:

        if booking["item_id"] != item_id:
            continue

        if dates_overlap(
            booking["delivery_date"],
            booking["return_date"],
            delivery_date,
            return_date
        ):
            booked_quantity += booking["quantity"]

    return booked_quantity


def check_bulk_availability(
    item_id,
    quantity,
    delivery_date,
    return_date
):
    item = get_item_by_id(item_id)

    if not item:
        raise ValueError("Item not found.")

    total_quantity = item["total_quantity"]

    booked_quantity = calculate_booked_quantity(
        item_id,
        delivery_date,
        return_date
    )

    available_quantity = (
        total_quantity - booked_quantity
    )

    return {
        "available": available_quantity >= quantity,
        "available_quantity": available_quantity
    }