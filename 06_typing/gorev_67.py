from typing import Callable
def islem_yap(a: int, b: int, fonksiyon: Callable[[int, int], int]) -> int:
    return fonksiyon(a, b)