from storage.json_storage import (
    load_bookings,
    save_bookings
)


def record_deposit(
    booking_id,
    amount
):
    if amount <= 0:
        raise ValueError(
            "Deposit amount must be greater than zero."
        )

    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            booking["deposit_paid"] += amount

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )


def set_discount(
    booking_id,
    discount_amount
):
    if discount_amount < 0:
        raise ValueError(
            "Discount cannot be negative."
        )

    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            if (
                discount_amount
                > booking["standard_total"]
            ):
                raise ValueError(
                    "Discount cannot exceed total amount."
                )

            booking["discount"] = (
                discount_amount
            )

            booking["final_total"] = (
                booking["standard_total"]
                - discount_amount
            )

            save_bookings(bookings)

            return booking

    raise ValueError(
        "Booking not found."
    )


def get_payment_summary(
    booking_id
):
    bookings = load_bookings()

    for booking in bookings:

        if booking["booking_id"] == booking_id:

            balance_due = (
                booking["final_total"]
                - booking["deposit_paid"]
            )

            if balance_due <= 0:
                payment_status = "paid"

            elif booking["deposit_paid"] > 0:
                payment_status = "partial"

            else:
                payment_status = "pending"

            summary = booking.copy()

            summary["balance_due"] = (
                balance_due
            )

            summary["payment_status"] = (
                payment_status
            )

            return summary

    raise ValueError(
        "Booking not found."
    )