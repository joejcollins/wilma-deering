"""Convert JSON files to a single CSV file."""

import csv
import json
import pathlib

from my_pkg import config


def main() -> None:
    """Convert JSON files to a single CSV file."""
    json_dir = pathlib.Path(config.RAW_DATA_DIR) / "cars"
    output_csv = (
        pathlib.Path(config.INTERIM_DATA_DIR) / "cars" / "01_mtcars.csv"
    )

    rows = []
    for json_path in sorted(json_dir.glob("*.json")):
        with json_path.open("r", encoding="utf-8") as f:
            row = json.load(f)
            rows.append(row)

    fieldnames = [
        "car",
        "id",
        "mpg",
        "cyl",
        "disp",
        "hp",
        "drat",
        "wt",
        "qsec",
        "vs",
        "am",
        "gear",
        "carb",
    ]

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with output_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_NONNUMERIC,
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output_csv}")


if __name__ == "__main__":
    main()
