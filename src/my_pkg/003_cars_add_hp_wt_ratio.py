"""Add horsepower-to-weight ratio to the interim MT Cars dataset."""

import csv
import pathlib

from my_pkg import config


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


def main() -> None:
    """Add horsepower-to-weight ratio to the interim MT Cars dataset."""
    input_csv = (
        pathlib.Path(config.INTERIM_DATA_DIR)
        / "cars"
        / "02_mtcars_with_manufacturer.csv"
    )
    output_csv = (
        pathlib.Path(config.INTERIM_DATA_DIR)
        / "cars"
        / "03_mtcars_with_manufacturer_and_ratio.csv"
    )

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    with input_csv.open("r", newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        fieldnames = list(reader.fieldnames or [])
        if "hp_to_wt_ratio" not in fieldnames:
            insert_pos = (
                fieldnames.index("wt") + 1
                if "wt" in fieldnames
                else len(fieldnames)
            )
            fieldnames.insert(insert_pos, "hp_to_wt_ratio")

        rows = []
        for row in reader:
            row["hp_to_wt_ratio"] = hp_to_weight_ratio(
                row.get("hp", ""), row.get("wt", "")
            )
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
