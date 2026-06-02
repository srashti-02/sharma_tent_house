from pathlib import Path

from src.utils.validators import (
    validate_item_name,
    validate_quantity,
    validate_price
)

from src.services.inventory_service import (
    add_item,
    get_all_items,
    search_item,
    update_quantity
)


def setup_function():
    Path("data").mkdir(exist_ok=True)

    with open("data/inventory.json", "w") as file:
        file.write("[]")


# ----------------------------
# Validator Tests
# ----------------------------

def test_validate_item_name():
    try:
        validate_item_name("")
        assert False
    except ValueError:
        assert True


def test_validate_quantity():
    try:
        validate_quantity(-5)
        assert False
    except ValueError:
        assert True


def test_validate_price():
    try:
        validate_price(-100)
        assert False
    except ValueError:
        assert True


def test_valid_values():
    validate_item_name("Plastic Chair")
    validate_quantity(100)
    validate_price(50)


# ----------------------------
# Service Layer Tests
# ----------------------------

def test_add_item():
    item = add_item(
        "Plastic Chair",
        "Furniture",
        100,
        50,
        200,
        "bulk"
    )

    items = get_all_items()

    assert len(items) == 1
    assert items[0]["item_name"] == "Plastic Chair"
    assert item["item_id"] == "ITEM_001"


def test_search_item():
    add_item(
        "Plastic Chair",
        "Furniture",
        100,
        50,
        200,
        "bulk"
    )

    results = search_item("Chair")

    assert len(results) == 1
    assert results[0]["item_name"] == "Plastic Chair"


def test_update_quantity():
    item = add_item(
        "Plastic Chair",
        "Furniture",
        100,
        50,
        200,
        "bulk"
    )

    update_quantity(
        item["item_id"],
        250
    )

    items = get_all_items()

    assert items[0]["total_quantity"] == 250


def test_auto_generated_item_ids():
    first_item = add_item(
        "Plastic Chair",
        "Furniture",
        100,
        50,
        200,
        "bulk"
    )

    second_item = add_item(
        "Steel Chair",
        "Furniture",
        50,
        60,
        200,
        "bulk"
    )

    assert first_item["item_id"] == "ITEM_001"
    assert second_item["item_id"] == "ITEM_002"