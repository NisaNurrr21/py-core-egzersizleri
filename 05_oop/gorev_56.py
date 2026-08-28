#  Çok Biçimlilik (Polymorphism)
def toplu_bildirim_gonder(bildirim_listesi: list) -> list:
    # Listedeki objelerin tipine bakmaksızın aynı metodu tetikliyoruz
    return [b.gonder() for b in bildirim_listesi]