import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_37 import dosyaya_ekle
def test_dosyaya_ekle(tmp_path):
    dosya = tmp_path / "log.txt"
    dosyaya_ekle(str(dosya), "Satir 1")
    dosyaya_ekle(str(dosya), "Satir 2")
    icerik = dosya.read_text(encoding="utf-8")
    assert "Satir 1\nSatir 2\n" in icerik