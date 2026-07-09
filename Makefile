# Consistent set of make tasks.
.DEFAULT_GOAL:=help  # because it's is a safe task.

clean: # Remove the environment.
	rm -rf .venv
	rm -rf *.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

.PHONY: data
data: # Process the data.
	.venv/bin/python src/my_pkg/001_cars_make_interim.py
	.venv/bin/python src/my_pkg/002_cars_add_manufacturer.py
	.venv/bin/python src/my_pkg/003_cars_add_hp_wt_ratio.py
	.venv/bin/python src/my_pkg/004_cars_create_parquet.py

.PHONY: docs
docs: # Serve the documentation.
	.venv/bin/mkdocs serve

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

lock:  # Create or update the requirements file.
	uv lock

publish:  # Publish the documentation to Github pages.
	.venv/bin/mkdocs gh-deploy --force --verbose

snake:	# Run the snakemake pipeline.
	.venv/bin/snakemake --cores 1

test:  # Run the unit tests.
	.venv/bin/pytest ./tests --verbose --color=yes

venv:  # Create the virtual environment.
	uv venv .venv --clear
	uv sync 
