# Snakemake DSL file - not valid Python syntax for type checkers

import my_pkg


CARS, = glob_wildcards(f"{my_pkg.config.RAW_DATA_DIR}/cars/{{car}}.json")

print(CARS)

rule all:
    input:
        "reports/cars_report.pdf",
        expand(
            f"{my_pkg.config.INTERIM_DATA_DIR}/cars/003_sorted_json/{{car}}.json",
            car=CARS
        )

rule add_guid:
    input:
        f"{my_pkg.config.RAW_DATA_DIR}/cars/{{car}}.json"
    output:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/001_guid/{{car}}.json"
    shell:
        "cars add-guid {input} {output}"

rule add_manufacturer:
    input:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/001_guid/{{car}}.json"
    output:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/002_manufacturer/{{car}}.json"
    shell:
        "cars add-manufacturer {input} {output}"

rule sort_and_format:
    input:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/002_manufacturer/{{car}}.json"
    output:
        f"{my_pkg.config.INTERIM_DATA_DIR}/cars/003_sorted_json/{{car}}.json"
    shell:
        "jq --sort-keys '.' {input} > {output}"

rule build_pdf:
    input:
        tex="latex/reports/cars_report.tex",
        figures=directory("latex/reports/figures")  # Re-runs pdf build if figures change
    output:
        pdf="latex/reports/cars_report.pdf"
    shell:
        """
        docker run --rm \
          -v "${{PWD}}:/workspace" \
          -w "/workspace/latex/reports" \
          ghcr.io/earthroverprogram/bragi:latest \
          pdflatex cars_report.tex
        """
