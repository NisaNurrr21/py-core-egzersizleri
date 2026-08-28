from contextlib import suppress
import os
def sessizce_sil(dosya_yolu: str):
    with suppress(FileNotFoundError):
        os.remove(dosya_yolu)