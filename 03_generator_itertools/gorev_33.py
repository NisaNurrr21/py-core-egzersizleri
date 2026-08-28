import itertools
def donguden_eleman_al(liste: list, adet: int) -> list:
    dongu = itertools.cycle(liste)
    return [next(dongu) for _ in range(adet)]