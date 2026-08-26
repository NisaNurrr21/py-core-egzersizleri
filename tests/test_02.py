import sys
from pathlib import Path

# Python'a klasör yolunu öğretiyoruz
sys.path.append(str(Path(__file__).parent.parent / "01_string_isleme"))

from gorev_02 import domain_cikar

def test_domain_cikar():
    assert domain_cikar("ornek@gmail.com") == "gmail.com"
    assert domain_cikar("iletisim@startup.com.tr") == "startup.com.tr"
    assert domain_cikar("hataligiris.com") == ""  # @ işareti yoksa boş dönmeli
    assert domain_cikar("@sadecedomain.com") == "sadecedomain.com"