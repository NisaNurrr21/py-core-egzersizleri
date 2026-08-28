def dosya_kopyala(kaynak_yol: str, hedef_yol: str):
    with open(kaynak_yol, "r", encoding="utf-8") as kaynak, \
         open(hedef_yol, "w", encoding="utf-8") as hedef:
        hedef.write(kaynak.read())