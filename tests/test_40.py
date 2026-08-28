import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_40 import sessizce_sil
def test_sessizce_sil(tmp_path):
    dosya = tmp_path / "silinecek.txt"
    dosya.write_text("sil beni")
    sessizce_sil(str(dosya))
    assert not dosya.exists()
    # Dosya zaten yoksa hata vermemeli (suppress çalışmalı)
    sessizce_sil(str(dosya))