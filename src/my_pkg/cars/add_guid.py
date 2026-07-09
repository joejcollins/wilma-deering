"""Add GUID to the cars data."""

import json
import pathlib

import uuid_extensions


def add_guid(input_json: pathlib.Path, output_json: pathlib.Path) -> None:
    """Add GUID to a single cars data set."""
    with input_json.open("r", encoding="utf-8") as f:
        car = json.load(f)
    car["guid"] = generate_guid()
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(car, f)


def generate_guid() -> str:
    """Generate a new GUID, we are using UUID7 because it is time-ordered."""
    return str(uuid_extensions.uuid7())
