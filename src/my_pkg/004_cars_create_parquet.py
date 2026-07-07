"""Create a final parquet file from the MT Cars dataset."""

import pathlib

import pyarrow.csv as pv
import pyarrow.parquet as pq

import config


def main() -> None:
    """Create a final parquet file from the MT Cars dataset."""
    input_csv = (
        pathlib.Path(config.INTERIM_DATA_DIR)
        / "cars"
        / "03_mtcars_with_manufacturer_and_ratio.csv"
    )
    output_parquet = (
        pathlib.Path(config.PROCESSED_DATA_DIR)
        / "cars"
        / "mtcars.parquet"
    )

    output_parquet.parent.mkdir(parents=True, exist_ok=True)

    table = pv.read_csv(input_csv)
    pq.write_table(table, output_parquet)

    print(f"Wrote {table.num_rows} rows to {output_parquet}")


if __name__ == "__main__":
    main()
