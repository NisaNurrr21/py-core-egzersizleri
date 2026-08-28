import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_38 import json_oku
import json
def test_json_oku(tmp_path):
    dosya = tmp_path / "veri.json"
    dosya.write_text('{"isim": "Nisa", "rol": "Backend"}', encoding="utf-8")
    assert json_oku(str(dosya)) == {"isim": "Nisa", "rol": "Backend"}
    assert json_oku(str(tmp_path / "olmayan.json")) == {}