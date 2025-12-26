import json
import os

def save_to_json(reviews, company, source):
    os.makedirs("data", exist_ok=True)
    filename = f"data/{company}_{source}_reviews.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)

    return filename
