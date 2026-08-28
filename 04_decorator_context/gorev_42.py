from contextlib import redirect_stdout
import io

def print_ciktisini_yakala(fonk) -> str:
    f = io.StringIO()
    with redirect_stdout(f):
        fonk()
    return f.getvalue().strip()