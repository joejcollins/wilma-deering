"""Configuration file for the project."""

from pathlib import Path

from dotenv import load_dotenv

from my_pkg.helpers import file_finder_service

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(file_finder_service.FileFinderService().find_root())

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "refined"
PROCESSED_DATA_DIR = DATA_DIR / "wrapped"

REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
