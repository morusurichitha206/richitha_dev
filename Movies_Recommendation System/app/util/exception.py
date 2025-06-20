import json
from pathlib import Path
from app.models.movies import Movies

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "movie.json"

def read_data():
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Movies(**movie) for movie in data]

def write_data(movies):
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in movies], f, indent=4)
