import os

DB_URL = os.environ.get("DB_URL", "sqlite://:memory:")
LOAD_DATA = os.environ.get("LOAD_DATA", "True") == "True"
DATA_PATH = os.environ.get(
    "DATA_PATH", "../data/data.csv"
)
