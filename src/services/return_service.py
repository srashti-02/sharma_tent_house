from datetime import datetime

from storage.json_storage import (
    load_bookings,
    save_bookings
)


def process_return(
    booking_id,
    actual_return_date
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            booking["actual_return_date"] = (
                actual_return_date
            )

            booking["booking_status"] = (
                "returned"
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )


def record_damage(
    booking_id,
    damaged_quantity,
    damage_fee
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            booking["damaged_quantity"] = (
                damaged_quantity
            )

            booking["damage_fee"] = (
                damage_fee
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )


def record_missing_items(
    booking_id,
    missing_quantity,
    replacement_fee
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            booking["missing_quantity"] = (
                missing_quantity
            )

            booking["replacement_fee"] = (
                replacement_fee
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )


def calculate_settlement(
    booking_id
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            balance_due = booking.get(
                "balance_due",
                0
            )

            damage_fee = booking.get(
                "damage_fee",
                0
            )

            replacement_fee = booking.get(
                "replacement_fee",
                0
            )

            settlement_total = (
                balance_due
                + damage_fee
                + replacement_fee
            )

            booking["settlement_total"] = (
                settlement_total
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )