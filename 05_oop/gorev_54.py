#  Soyut Sınıflar (Abstract Classes - abc)
from abc import ABC, abstractmethod

class Bildirim(ABC):
    @abstractmethod
    def gonder(self) -> str:
        pass

class SMSBildirim(Bildirim):
    def gonder(self) -> str:
        return "SMS İletildi"