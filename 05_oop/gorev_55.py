#  Çoklu Kalıtım (Multiple Inheritance)
class Raporlanabilir:
    def rapor_uret(self): return "Rapor Hazır"

class Yazdirilabilir:
    def yazdir(self): return "Yazıcıya Gönderildi"

class SatisBelgesi(Raporlanabilir, Yazdirilabilir):
    pass