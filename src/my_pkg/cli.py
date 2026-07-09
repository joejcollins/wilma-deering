"""CLI for car data processing."""

import pathlib

import typer

from my_pkg.cars import add_guid

app = typer.Typer()


@app.command()
def add_guid_to_cars(
    input_path: pathlib.Path = typer.Argument(..., help="Input JSON file"),
    output_path: pathlib.Path = typer.Argument(..., help="Output JSON file"),
) -> None:
    """Add GUID values to a cars dataset.

    Reads a JSON input file and writes a CSV output file.

    Example:
        add-guid-to-cars data/raw/cars.json data/interim/cars.csv

    """
    add_guid.add_guid(input_path, output_path)


@app.command()
def hello():
    """Print hello to the console."""
    print("Hello")
