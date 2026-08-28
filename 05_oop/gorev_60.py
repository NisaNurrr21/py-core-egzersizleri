# @dataclass ile Veri Odaklı Sınıf (Otomatik __init__ ve __repr__)
from dataclasses import dataclass

@dataclass
class KampanyaKodu:
    kod: str
    indirim_orani: float
    aktif_mi: bool = True