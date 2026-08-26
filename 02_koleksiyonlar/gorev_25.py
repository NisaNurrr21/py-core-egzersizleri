def sadece_benzersizler(liste: list) -> list:
    return [x for x in liste if liste.count(x) == 1]