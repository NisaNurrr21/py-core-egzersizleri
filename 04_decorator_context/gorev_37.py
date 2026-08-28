def dosyaya_ekle(dosya_yolu: str, satir: str):
    with open(dosya_yolu, "a", encoding="utf-8") as dosya:
        dosya.write(satir + "\n")