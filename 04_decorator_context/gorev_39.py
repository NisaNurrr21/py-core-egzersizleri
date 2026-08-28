import time
class Zamanlayici:
    def __enter__(self):
        self.baslangic = time.time()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sure = time.time() - self.baslangic