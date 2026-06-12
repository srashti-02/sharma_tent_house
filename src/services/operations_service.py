from datetime import date

from storage.json_storage import (
    load_bookings
)


def get_todays_deliveries():
    today = str(date.today())

    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("delivery_date") == today
    ]


def get_todays_collections():
    today = str(date.today())

    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("return_date") == today
    ]


def get_active_bookings():
    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get(
            "booking_status",
            "active"
        ) == "active"
    ]


def get_rented_inventory():
    bookings = get_active_bookings()

    inventory = {}

    for booking in bookings:

        item_id = booking["item_id"]

        inventory[item_id] = (
            inventory.get(item_id, 0)
            + booking["quantity"]
        )

    return inventory