from storage.json_storage import (
    load_inventory,
    save_inventory
)

from utils.validators import (
    validate_item_name,
    validate_category,
    validate_quantity,
    validate_price,
    validate_item_type,
    validate_item_status
)


def generate_item_id():
    inventory = load_inventory()

    if not inventory:
        return "ITEM_001"

    max_number = 0

    for item in inventory:
        try:
            number = int(
                item["item_id"].replace(
                    "ITEM_",
                    ""
                )
            )

            max_number = max(
                max_number,
                number
            )

        except (
            ValueError,
            KeyError
        ):
            continue

    return f"ITEM_{max_number + 1:03d}"


def add_item(
    item_name,
    category,
    total_quantity,
    standard_rent_per_day,
    damage_charge,
    item_type,
    item_status="active"
):
    inventory = load_inventory()

    validate_item_name(
        item_name
    )
    validate_category(
        category
    )
    validate_quantity(
        total_quantity
    )
    validate_price(
        standard_rent_per_day
    )
    validate_price(
        damage_charge
    )
    validate_item_type(
        item_type
    )
    validate_item_status(
        item_status
    )

    new_item = {
        "item_id":
            generate_item_id(),
        "item_name":
            item_name,
        "category":
            category,
        "total_quantity":
            total_quantity,
        "standard_rent_per_day":
            standard_rent_per_day,
        "damage_charge":
            damage_charge,
        "item_type":
            item_type,
        "item_status":
            item_status
    }

    inventory.append(
        new_item
    )

    save_inventory(
        inventory
    )

    return new_item


def get_all_items(
    include_inactive=False
):
    inventory = load_inventory()

    if include_inactive:
        return inventory

    return [
        item
        for item in inventory
        if item.get(
            "item_status",
            "active"
        ) == "active"
    ]


def search_item(
    item_name
):
    inventory = get_all_items()

    return [
        item
        for item in inventory
        if (
            item_name.lower()
            in item[
                "item_name"
            ].lower()
        )
    ]


def get_item_by_id(
    item_id
):
    inventory = load_inventory()

    for item in inventory:
        if (
            item.get(
                "item_id"
            )
            == item_id
        ):
            return item

    return None


def update_item(
    item_id,
    item_name=None,
    category=None,
    total_quantity=None,
    standard_rent_per_day=None,
    damage_charge=None,
    item_type=None,
    item_status=None
):
    inventory = load_inventory()

    for item in inventory:
        if (
            item["item_id"]
            == item_id
        ):
            if item_name:
                validate_item_name(
                    item_name
                )
                item[
                    "item_name"
                ] = item_name

            if category:
                validate_category(
                    category
                )
                item[
                    "category"
                ] = category

            if (
                total_quantity
                is not None
            ):
                validate_quantity(
                    total_quantity
                )
                item[
                    "total_quantity"
                ] = total_quantity

            if (
                standard_rent_per_day
                is not None
            ):
                validate_price(
                    standard_rent_per_day
                )
                item[
                    "standard_rent_per_day"
                ] = (
                    standard_rent_per_day
                )

            if (
                damage_charge
                is not None
            ):
                validate_price(
                    damage_charge
                )
                item[
                    "damage_charge"
                ] = (
                    damage_charge
                )

            if item_type:
                validate_item_type(
                    item_type
                )
                item[
                    "item_type"
                ] = item_type

            if item_status:
                validate_item_status(
                    item_status
                )
                item[
                    "item_status"
                ] = item_status

            save_inventory(
                inventory
            )

            return item

    raise ValueError(
        "Item not found."
    )


def delete_item(
    item_id
):
    inventory = load_inventory()

    for item in inventory:
        if (
            item["item_id"]
            == item_id
        ):
            item[
                "item_status"
            ] = "inactive"

            save_inventory(
                inventory
            )

            return item

    raise ValueError(
        "Item not found."
    )


def update_quantity(
    item_id,
    new_quantity
):
    validate_quantity(
        new_quantity
    )

    inventory = load_inventory()

    for item in inventory:
        if (
            item["item_id"]
            == item_id
        ):
            item[
                "total_quantity"
            ] = new_quantity

            save_inventory(
                inventory
            )

            return item

    raise ValueError(
        "Item not found."
    )


def update_item_status(
    item_id,
    status
):
    inventory = load_inventory()

    for item in inventory:
        if (
            item["item_id"]
            == item_id
        ):
            validate_item_status(
                status
            )

            item[
                "item_status"
            ] = status

            save_inventory(
                inventory
            )

            return item

    raise ValueError(
        "Item not found."
    )