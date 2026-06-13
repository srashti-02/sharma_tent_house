from storage.json_storage import (
    load_bookings,
    load_inventory
)


def revenue_report():
    bookings = load_bookings()

    total_revenue = sum(
        booking.get("final_total", 0)
        for booking in bookings
    )

    total_deposits = sum(
        booking.get("deposit_paid", 0)
        for booking in bookings
    )

    total_balance = sum(
    booking["final_total"]
    - booking["deposit_paid"]
    for booking in bookings
)

    return {
        "total_revenue": total_revenue,
        "total_deposits": total_deposits,
        "outstanding_balance": total_balance
    }


def damage_report():
    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("damage_fee", 0) > 0
    ]


def missing_inventory_report():
    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("replacement_fee", 0) > 0
    ]


def returned_booking_report():
    bookings = load_bookings()

    returned = [
        booking
        for booking in bookings
        if booking.get("booking_status")
        == "returned"
    ]

    total_settlement = sum(
        booking.get(
            "settlement_total",
            0
        )
        for booking in returned
    )

    return {
        "total_returned": len(returned),
        "total_settlement": total_settlement
    }


def inventory_utilization_report():
    bookings = load_bookings()

    rented = {}

    for booking in bookings:

        item_id = booking["item_id"]

        rented[item_id] = (
            rented.get(item_id, 0)
            + booking["quantity"]
        )

    if not rented:
        return {}

    most_rented = max(
        rented,
        key=rented.get
    )

    least_rented = min(
        rented,
        key=rented.get
    )

    return {
        "most_rented": most_rented,
        "least_rented": least_rented
    }