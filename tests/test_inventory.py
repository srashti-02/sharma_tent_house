from src.utils.validators import (
    validate_item_name,
    validate_quantity,
    validate_price
)

from pathlib import Path
import sys

sys.path.append(
    str(Path(__file__).resolve().parent.parent / "src")
)

from services.inventory_service import (
    add_item,
    get_all_items,
    search_item,
    update_quantity
)


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
# Service Tests
# ----------------------------

def test_add_item():
    item = add_item(
        "Test Chair",
        "Furniture",
        100,
        50,
        200,
        "bulk"
    )

    assert item["item_name"] == "Test Chair"


def test_search_item():
    results = search_item("Chair")
    assert isinstance(results, list)


def test_update_quantity():
    items = get_all_items()

    if items:
        item_id = items[0]["item_id"]

        update_quantity(
            item_id,
            999
        )

        updated_items = get_all_items()

        assert updated_items[0]["total_quantity"] == 999