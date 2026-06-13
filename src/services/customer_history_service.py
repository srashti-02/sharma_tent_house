from storage.json_storage import load_bookings


def get_customer_history(customer_id):
    bookings = load_bookings()

    return [
        booking
        for booking in bookings
        if booking.get("customer_id") == customer_id
    ]