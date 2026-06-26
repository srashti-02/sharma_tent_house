def validate_item_name(name):
    if not name.strip():
        raise ValueError("Item name cannot be empty.")


def validate_quantity(quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")


def validate_price(price):
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
def validate_item_id(item_id):
    if not item_id.strip():
        raise ValueError("Item ID cannot be empty.")

def validate_phone(phone):
    phone = phone.strip()

    if (
        not phone.isdigit()
        or len(phone) != 10
    ):
        raise ValueError(
            "Phone number must contain exactly 10 digits."
        )
    
def validate_category(category):
    if not category.strip():
        raise ValueError("Category cannot be empty.")


def validate_item_type(item_type):
    valid_types = [
        "bulk",
        "limited",
        "unique"
    ]

    if item_type.lower() not in valid_types:
        raise ValueError(
            "Item type must be bulk, limited, or unique."
        )


def validate_item_status(item_status):
    valid_statuses = [
        "active",
        "inactive"
    ]

    if item_status.lower() not in valid_statuses:
        raise ValueError(
            "Item status must be active or inactive."
        )