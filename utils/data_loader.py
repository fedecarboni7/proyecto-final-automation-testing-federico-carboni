import json
import csv


def load_users_from_json(filepath="data/users.json"):
    """Load and return the list of users from the JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)


def load_checkout_data_from_csv(filepath="data/checkout_data.csv"):
    """Load and return a list of dictionaries from the CSV file."""
    with open(filepath, "r") as f:
        return list(csv.DictReader(f))
