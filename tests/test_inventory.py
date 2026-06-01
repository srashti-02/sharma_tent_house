from src.utils.validators import (
    validate_item_name,
    validate_quantity,
    validate_price
)


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