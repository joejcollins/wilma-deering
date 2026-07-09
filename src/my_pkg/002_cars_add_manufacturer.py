"""Add derived features to the interim MT Cars dataset."""

import csv
import pathlib

from my_pkg import config


def extract_manufacturer(car_name: str) -> str:
    """Extract the manufacturer from the first word of a car name."""
    return car_name.strip().split()[0] if car_name else ""


def main() -> None:
    """Add derived features to the interim MT Cars dataset."""
    input_csv = pathlib.Path(config.INTERIM_DATA_DIR) / "cars" / "01_mtcars.csv"
    output_csv = (
        pathlib.Path(config.INTERIM_DATA_DIR)
        / "cars"
        / "02_mtcars_with_manufacturer.csv"
    )

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    with input_csv.open("r", newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        fieldnames = list(reader.fieldnames or [])
        if "manufacturer" not in fieldnames:
            insert_pos = (
                fieldnames.index("car") + 1
                if "car" in fieldnames
                else len(fieldnames)
            )
            fieldnames.insert(insert_pos, "manufacturer")

        rows = []
        for row in reader:
            row["manufacturer"] = extract_manufacturer(row.get("car", ""))
            rows.append(row)

    with output_csv.open("w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(
            f_out, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {output_csv}")


if __name__ == "__main__":
    main()
