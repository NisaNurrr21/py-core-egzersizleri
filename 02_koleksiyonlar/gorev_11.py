def numara_tekillestir(numaralar: list) -> list:
    # Set'ler sırayı bozar, bu yüzden sırayı koruyan dict.fromkeys kullanıyoruz
    return list(dict.fromkeys(numaralar))