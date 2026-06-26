from datetime import datetime

from storage.json_storage import (
    load_bookings,
    save_bookings
)


def process_return(
    booking_id,
    actual_return_date,
    actual_return_time
):
    bookings = load_bookings()

    for booking in bookings:
        if (
            booking["booking_id"]
            == booking_id
        ):
            booking[
                "actual_return_date"
            ] = actual_return_date

            booking[
                "actual_return_time"
            ] = actual_return_time

            booking[
                "booking_status"
            ] = "returned"

            save_bookings(
                bookings
            )

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
        if (
            booking["booking_id"]
            == booking_id
        ):
            if (
                booking.get(
                    "booking_status"
                )
                != "returned"
            ):
                raise ValueError(
                    "Booking must be returned first."
                )

            booking[
                "damaged_quantity"
            ] = damaged_quantity

            booking[
                "damage_fee"
            ] = damage_fee

            save_bookings(
                bookings
            )

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
        if (
            booking["booking_id"]
            == booking_id
        ):
            if (
                booking.get(
                    "booking_status"
                )
                != "returned"
            ):
                raise ValueError(
                    "Booking must be returned first."
                )

            booking[
                "missing_quantity"
            ] = missing_quantity

            booking[
                "replacement_fee"
            ] = replacement_fee

            save_bookings(
                bookings
            )

            return booking

    raise ValueError(
        "Booking not found."
    )


def calculate_late_fee(
    booking_id,
    hourly_late_fee=50
):
    bookings = load_bookings()

    for booking in bookings:
        if (
            booking["booking_id"]
            == booking_id
        ):
            actual_date = booking.get(
                "actual_return_date"
            )

            actual_time = booking.get(
                "actual_return_time"
            )

            if (
                not actual_date
                or not actual_time
            ):
                raise ValueError(
                    "Booking not returned yet."
                )

            expected_datetime = (
                datetime.strptime(
                    f"{booking['return_date']} "
                    f"{booking['return_time']}",
                    "%Y-%m-%d %H:%M"
                )
            )

            actual_datetime = (
                datetime.strptime(
                    f"{actual_date} "
                    f"{actual_time}",
                    "%Y-%m-%d %H:%M"
                )
            )

            difference = (
                actual_datetime
                - expected_datetime
            )

            late_hours = int(
                difference.total_seconds()
                // 3600
            )

            if late_hours < 0:
                late_hours = 0

            late_fee = (
                late_hours
                * hourly_late_fee
            )

            booking[
                "late_hours"
            ] = late_hours

            booking[
                "late_fee"
            ] = late_fee

            save_bookings(
                bookings
            )

            return booking

    raise ValueError(
        "Booking not found."
    )


def calculate_settlement(
    booking_id
):
    bookings = load_bookings()

    for booking in bookings:
        if (
            booking["booking_id"]
            == booking_id
        ):
            pending_amount = (
                booking.get(
                    "pending_amount",
                    0
                )
            )

            damage_fee = (
                booking.get(
                    "damage_fee",
                    0
                )
            )

            replacement_fee = (
                booking.get(
                    "replacement_fee",
                    0
                )
            )

            late_fee = (
                booking.get(
                    "late_fee",
                    0
                )
            )

            settlement_total = (
                pending_amount
                + damage_fee
                + replacement_fee
                + late_fee
            )

            booking[
                "settlement_total"
            ] = settlement_total

            save_bookings(
                bookings
            )

            return booking

    raise ValueError(
        "Booking not found."
    )