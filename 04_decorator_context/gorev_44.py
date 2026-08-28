class MockVeritabani:
    def __init__(self):
        self.bagli_mi = False
    
    def __enter__(self):
        self.bagli_mi = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.bagli_mi = False