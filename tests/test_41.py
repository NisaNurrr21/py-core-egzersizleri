import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "04_decorator_context"))
from gorev_41 import gecici_ayar
def test_gecici_ayar():
    config = {"tema": "karanlik"}
    with gecici_ayar(config, "tema", "aydinlik"):
        assert config["tema"] == "aydinlik"
    assert config["tema"] == "karanlik" # Blok bitince eskiye dönmeli