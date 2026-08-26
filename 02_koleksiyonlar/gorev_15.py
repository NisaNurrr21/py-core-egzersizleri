def en_cok_harcayanlari_sirala(musteri_listesi: list) -> list:
    # lambda x: x[1] ifadesi, listenin içindeki her bir elemanın 2. değerine (indeks 1, yani fiyata) bak demektir.
    # reverse=True ise sıralamayı küçükten büyüğe değil, büyükten küçüğe yapar.
    return sorted(musteri_listesi, key=lambda x: x[1], reverse=True)