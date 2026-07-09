"""Add features to the cars data."""

import json
import pathlib

import uuid_extensions


def add_a_feature(
    input_json: pathlib.Path, output_json: pathlib.Path, transform=None
) -> None:
    """Add a feature to a single cars dataset and write to file."""
    if transform is None:
        transform = add_guid

    with input_json.open("r", encoding="utf-8") as f:
        car = json.load(f)
    car = transform(car)
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(car, f)


def add_guid(car: dict) -> dict:
    """Pure function: add GUID to car data."""
    car_with_guid = car.copy()
    car_with_guid["guid"] = str(uuid_extensions.uuid7())
    return car_with_guid
