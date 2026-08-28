import json
def json_oku(dosya_yolu: str) -> dict:
    try:
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}