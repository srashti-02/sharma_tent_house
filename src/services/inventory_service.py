from storage.json_storage import load_inventory, save_inventory
from utils.validators import (
    validate_item_name,
    validate_quantity,
    validate_price
)


def add_item(
    item_id,
    item_name,
    category,
    total_quantity,
    standard_rent_per_day,
    damage_charge,
    item_type,
    item_status="active"
):
    inventory = load_inventory()

    for item in inventory:
        if item["item_id"] == item_id:
            raise ValueError("Item ID already exists.")

    validate_item_name(item_name)
    validate_quantity(total_quantity)
    validate_price(standard_rent_per_day)
    validate_price(damage_charge)

    new_item = {
        "item_id": item_id,
        "item_name": item_name,
        "category": category,
        "total_quantity": total_quantity,
        "standard_rent_per_day": standard_rent_per_day,
        "damage_charge": damage_charge,
        "item_type": item_type,
        "item_status": item_status
    }

    inventory.append(new_item)
    save_inventory(inventory)

    return new_item


# STEP 6
def get_all_items():
    return load_inventory()


# STEP 7
def search_item(item_name):
    inventory = load_inventory()

    results = []

    for item in inventory:
        if item_name.lower() in item["item_name"].lower():
            results.append(item)

    return results


# STEP 8
def update_quantity(item_id, new_quantity):
    validate_quantity(new_quantity)

    inventory = load_inventory()

    for item in inventory:
        if item["item_id"] == item_id:
            item["total_quantity"] = new_quantity

            save_inventory(inventory)
            return

    raise ValueError("Item not found.")