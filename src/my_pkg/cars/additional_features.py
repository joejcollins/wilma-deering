"""Add new features to the cars dataset."""

import json
import pathlib


def add_features(input_json: pathlib.Path, output_json: pathlib.Path) -> None:
    """Add new features to the cars dataset."""
    with input_json.open("r", encoding="utf-8") as f:
        car = json.load(f)
    car["hp_to_weight_ratio"] = hp_to_weight_ratio(car["hp"], car["wt"])
    car["manufacturer"] = extract_manufacturer(car["car"])
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(car, f)


def hp_to_weight_ratio(hp_value: str, wt_value: str) -> str:
    """Return horsepower-to-weight ratio as a string, or empty if invalid."""
    try:
        hp = float(hp_value)
        wt = float(wt_value)
        if wt == 0:
            return ""
        return str(hp / wt)
    except TypeError, ValueError:
        return ""


def extract_manufacturer(car_name: str) -> str:
    """Extract the manufacturer from the first word of a car name."""
    if not car_name:
        return ""
    return car_name.strip().split()[0]
