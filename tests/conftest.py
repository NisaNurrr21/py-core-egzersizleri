import sys
from pathlib import Path

# Proje ana dizinini buluyoruz (tests klasörünün bir üstü)
proje_dizini = Path(__file__).parent.parent

# Ana dizini yola ekle
sys.path.insert(0, str(proje_dizini))

# Proje dizinindeki tüm alt klasörleri (01_, 02_ vb.) tek tek bulup Python'un arama yoluna (sys.path) ekliyoruz
for alt_klasor in proje_dizini.iterdir():
    # Gizli klasörleri (.venv, .git vb.) ve tests klasörünü atla, sadece görev klasörlerini ekle
    if alt_klasor.is_dir() and not alt_klasor.name.startswith(".") and alt_klasor.name != "tests":
        sys.path.insert(0, str(alt_klasor))
