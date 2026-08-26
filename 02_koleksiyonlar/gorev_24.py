def harf_frekansi(kelime: str) -> dict:
    return {harf: kelime.count(harf) for harf in set(kelime)}