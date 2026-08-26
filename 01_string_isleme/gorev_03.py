def palindrom_mu(metin: str)-> bool:

     kucuk_metin = metin.lower()

     return kucuk_metin == kucuk_metin[::-1]