import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_39 import Zamanlayici
import time
def test_zamanlayici():
    with Zamanlayici() as z:
        time.sleep(0.1)
    assert z.sure >= 0.1