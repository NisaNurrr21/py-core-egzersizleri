def dosyaya_yaz(dosya_yolu: str, icerik: str):
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.write(icerik)