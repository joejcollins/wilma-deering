SRC_DIR = "src"
RAW_DATA_DIR = "data/raw/cars"
INTERIM_DIR = "data/refined/cars"
PROCESSED_DIR = "data/wrapped/cars"

import pathlib

import my_pkg

rule all:
    input:
        f"{PROCESSED_DIR}/mtcars.parquet"

rule make_interim:
    input:
        # Trigger on the raw directory contents so reruns happen when JSON files change.
        pathlib.Path(my_pkg.config.RAW_DATA_DIR) / "cars"
    output:
        f"{INTERIM_DIR}/01_mtcars.csv"
    shell:
        "PYTHONPATH={SRC_DIR} python {SRC_DIR}/my_pkg/001_cars_make_interim.py"

rule add_manufacturer:
    input:
        f"{INTERIM_DIR}/01_mtcars.csv"
    output:
        f"{INTERIM_DIR}/02_mtcars_with_manufacturer.csv"
    shell:
        "PYTHONPATH={SRC_DIR} python {SRC_DIR}/my_pkg/002_cars_add_manufacturer.py"

rule add_ratio:
    input:
        f"{INTERIM_DIR}/02_mtcars_with_manufacturer.csv"
    output:
        f"{INTERIM_DIR}/03_mtcars_with_manufacturer_and_ratio.csv"
    shell:
        "PYTHONPATH={SRC_DIR} python {SRC_DIR}/my_pkg/003_cars_add_hp_wt_ratio.py"

rule create_parquet:
    input:
        f"{INTERIM_DIR}/03_mtcars_with_manufacturer_and_ratio.csv"
    output:
        f"{PROCESSED_DIR}/mtcars.parquet"
    shell:
        "PYTHONPATH={SRC_DIR} python {SRC_DIR}/my_pkg/004_cars_create_parquet.py"
