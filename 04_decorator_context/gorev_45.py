import os
from contextlib import contextmanager

@contextmanager
def gecici_dizin(hedef_dizin: str):
    eski_dizin = os.getcwd()
    os.chdir(hedef_dizin)
    try:
        yield
    finally:
        os.chdir(eski_dizin)