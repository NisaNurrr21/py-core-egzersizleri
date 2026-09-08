from typing import TypeVar, List

# T adında esnek bir tip değişkeni oluşturuyoruz
T = TypeVar('T')

def ilk_elemani_getir(liste: List[T]) -> T:
    """
    İçine hangi tipte liste girerse, dönüş tipi de otomatik olarak o tip olur.
    Örn: List[int] girerse int döner, List[str] girerse str döner.
    """
    if not liste:
        raise ValueError("Liste boş olamaz")
    return liste[0]