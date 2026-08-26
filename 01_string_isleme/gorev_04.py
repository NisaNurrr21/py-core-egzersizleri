def veriyi_maskele(veri: str) -> str:
    
    if len(veri) <= 4:
        return veri
    
   
    yildiz_kismi = "*" * (len(veri) - 4)
    return f"{veri[:2]}{yildiz_kismi}{veri[-2:]}"