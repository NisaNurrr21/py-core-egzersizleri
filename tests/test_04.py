import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))
from gorev_04 import veriyi_maskele

def test_veriyi_maskele():
    assert veriyi_maskele("123456789") == "12*****89"
    assert veriyi_maskele("Nisa") == "Nisa"  # Sadece baştan 2, sondan 2 (4 harfse böyle olur, aslında 'Ni' 'sa' ortada harf kalmaz, testte ufak bir numara var!) 
    # Düzeltme: "Nisa" için dönen değerin tam ortasında yıldız olmamalı, bu testin hatası. Şöyle yapalım:
    assert veriyi_maskele("NisaNur") == "Ni***ur"
    assert veriyi_maskele("Can") == "Can"