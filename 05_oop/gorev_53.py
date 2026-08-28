# @staticmethod ile Sınıfa Bağımsız Yardımcı Metot
class Dogrulama:
    @staticmethod
    def tc_gecerli_mi(tc: str) -> bool:
        return len(tc) == 11 and tc.isdigit()