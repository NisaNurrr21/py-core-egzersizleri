import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_43 import dosya_kopyala
def test_dosya_kopyala(tmp_path):
    kaynak = tmp_path / "kaynak.txt"
    hedef = tmp_path / "hedef.txt"
    kaynak.write_text("Kopyalanacak Veri", encoding="utf-8")
    
    dosya_kopyala(str(kaynak), str(hedef))
    assert hedef.read_text(encoding="utf-8") == "Kopyalanacak Veri"