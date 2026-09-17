import sys
from pathlib import Path

# Proje ana dizinini sys.path'e ekler, 80 testin hepsinde otomatik çalışır
proje_dizini = Path(__file__).parent.parent
sys.path.insert(0, str(proje_dizini))
