import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_05 import slug_olustur

def test_slug_olustur():
    assert slug_olustur("  Python Backend Egzersizleri  ") == "python-backend-egzersizleri"
    assert slug_olustur("FastAPI ile API Gelistirme") == "fastapi-ile-api-gelistirme"