# Snakemake DSL file - not valid Python syntax for type checkers

import my_pkg

from my_pkg.cars import add_guid


CARS, = glob_wildcards(f"{my_pkg.config.RAW_DATA_DIR}/cars/{{car}}.json")

print(CARS)

rule all:
    input:
        expand(
            f"{my_pkg.config.INTERIM_DATA_DIR}/cars/002_sorted_json/{{car}}.json",
            car=CARS
        )


rule add_guid:
    input:
        f"{my_pkg.config.RAW_DATA_DIR}/cars/{{car}}.json"
    output:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/001_guid/{{car}}.json"
    shell:
        "cars add-guid-to-cars {input} {output}"

rule sort_and_format:
    input:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/001_guid/{{car}}.json"
    output:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/002_sorted_json/{{car}}.json"
    shell:
        "jq --sort-keys '.' {input} > {output}"

# rule all:
#     input:
#         f"{PROCESSED_DIR}/mtcars.parquet"

# rule make_interim:
#     input:
#         expand(f"{RAW_DATA_DIR}/{{name}}.json", name=RAW_JSONS)
#     output:
#         f"{INTERIM_DIR}/01_mtcars.csv"
#     script:
#         "./src/my_pkg/001_cars_make_interim.py"

# rule add_manufacturer:
#     input:
#         f"{INTERIM_DIR}/01_mtcars.csv"
#     output:
#         f"{INTERIM_DIR}/02_mtcars_with_manufacturer.csv"
#     run:
#         "./src/my_pkg/002_cars_add_manufacturer.py"

# rule add_ratio:
#     input:
#         f"{INTERIM_DIR}/02_mtcars_with_manufacturer.csv"
#     output:
#         f"{INTERIM_DIR}/03_mtcars_with_manufacturer_and_ratio.csv"
#     script:
#         "./src/my_pkg/003_cars_add_hp_wt_ratio.py"

# rule create_parquet:
#     input:
#         f"{INTERIM_DIR}/03_mtcars_with_manufacturer_and_ratio.csv"
#     output:
#         f"{PROCESSED_DIR}/mtcars.parquet"
#     script:
#         "./src/my_pkg/004_cars_create_parquet.py"
