import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_36 import dosyaya_yaz
def test_dosyaya_yaz(tmp_path):
    dosya = tmp_path / "test.txt"
    dosyaya_yaz(str(dosya), "Backend API")
    assert dosya.read_text(encoding="utf-8") == "Backend API"