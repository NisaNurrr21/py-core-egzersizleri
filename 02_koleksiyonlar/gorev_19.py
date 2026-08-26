def min_max_bul(sayilar: list) -> tuple:
    if not sayilar:
        return (0, 0)
    return (min(sayilar), max(sayilar))