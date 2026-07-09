"""CLI for car data processing."""

import pathlib

import typer

from my_pkg.cars import add_features

app = typer.Typer()


@app.command()
def add_guid(
    input_path: pathlib.Path = typer.Argument(..., help="Input JSON file"),
    output_path: pathlib.Path = typer.Argument(..., help="Output JSON file"),
) -> None:
    """Add GUID to a cars dataset.

    Reads a JSON input file and writes a JSON output file.

    Example:
        add-guid-to-cars data/raw/cars.json data/interim/cars.json

    """
    add_features.add_a_feature(
        input_path, output_path, transform=add_features.add_guid
    )


@app.command()
def add_manufacturer(
    input_path: pathlib.Path = typer.Argument(..., help="Input JSON file"),
    output_path: pathlib.Path = typer.Argument(..., help="Output JSON file"),
) -> None:
    """Add manufacturer to a cars dataset.

    Reads a JSON input file and writes a JSON output file.

    Example:
        add-manufacturer-to-cars data/raw/cars.json data/interim/cars.json

    """
    add_features.add_a_feature(
        input_path, output_path, transform=add_features.add_manufacturer
    )
