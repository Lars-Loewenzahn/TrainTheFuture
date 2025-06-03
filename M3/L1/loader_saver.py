import json
from typing import Any


def load_json(filepath: str) -> Any:
    """Lädt eine JSON-Datei und gibt den Inhalt zurück."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath: str, data: Any) -> None:
    """Speichert Daten als JSON-Datei."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


path = "M3\L1\exsample.json"
data = load_json(path)
print(data)
data["name"] = "Bernd"
print(data)