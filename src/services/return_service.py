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
    if damaged_quantity <= 0:
        raise ValueError(
            "Damaged quantity must be greater than zero."
        )

    if damage_fee < 0:
        raise ValueError(
            "Damage fee cannot be negative."
        )

    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if (
                booking.get(
                    "booking_status",
                    "active"
                )
                != "returned"
            ):
                raise ValueError(
                    "Booking must be returned before recording damage."
                )

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
    if missing_quantity <= 0:
        raise ValueError(
            "Missing quantity must be greater than zero."
        )

    if replacement_fee < 0:
        raise ValueError(
            "Replacement fee cannot be negative."
        )

    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if (
                booking.get(
                    "booking_status",
                    "active"
                )
                != "returned"
            ):
                raise ValueError(
                    "Booking must be returned before recording missing items."
                )

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


def calculate_late_fee(
    booking_id,
    daily_late_fee=100
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            actual_return = booking.get(
                "actual_return_date"
            )

            if not actual_return:
                raise ValueError(
                    "Booking not returned yet."
                )

            expected_date = datetime.strptime(
                booking["return_date"],
                "%Y-%m-%d"
            )

            actual_date = datetime.strptime(
                actual_return,
                "%Y-%m-%d"
            )

            late_days = (
                actual_date - expected_date
            ).days

            if late_days < 0:
                late_days = 0

            late_fee = (
                late_days * daily_late_fee
            )

            booking["late_days"] = (
                late_days
            )

            booking["late_fee"] = (
                late_fee
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

            balance_due = (
                booking.get(
                    "final_total",
                    0
                )
                - booking.get(
                    "deposit_paid",
                    0
                )
            )

            damage_fee = booking.get(
                "damage_fee",
                0
            )

            replacement_fee = booking.get(
                "replacement_fee",
                0
            )

            late_fee = booking.get(
                "late_fee",
                0
            )

            settlement_total = (
                balance_due
                + damage_fee
                + replacement_fee
                + late_fee
            )

            booking["settlement_total"] = (
                settlement_total
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )