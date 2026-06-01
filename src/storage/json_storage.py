import json
from pathlib import Path

DATA_FILE = Path("data/inventory.json")


def load_inventory():
    """
    Load inventory data from JSON file.
    """
    try:
        if not DATA_FILE.exists():
            DATA_FILE.parent.mkdir(exist_ok=True)
            DATA_FILE.write_text("[]")

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Error: inventory.json is corrupted.")
        return []


def save_inventory(inventory):
    """
    Save inventory data to JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(inventory, file, indent=4)