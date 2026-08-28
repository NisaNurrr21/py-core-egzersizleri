def kareleri_uret(sayilar: list):
    # Köşeli parantez (list comprehension) yerine normal parantez kullanıldığında generator olur
    return (x * x for x in sayilar)