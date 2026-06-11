import json
from pathlib import Path

INVENTORY_FILE = Path("data/inventory.json")
BOOKINGS_FILE = Path("data/bookings.json")


def _load_json(file_path: Path):
    # Ensure directory and file exist
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("[]")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: {file_path.name} is corrupted.")
        return []


def _save_json(file_path: Path, data):
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_inventory():
    return _load_json(INVENTORY_FILE)


def save_inventory(inventory):
    _save_json(INVENTORY_FILE, inventory)


def load_bookings():
    return _load_json(BOOKINGS_FILE)


def save_bookings(bookings):
    _save_json(BOOKINGS_FILE, bookings)
