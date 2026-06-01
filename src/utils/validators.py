def validate_item_name(name):
    if not name.strip():
        raise ValueError("Item name cannot be empty.")


def validate_quantity(quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")


def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")