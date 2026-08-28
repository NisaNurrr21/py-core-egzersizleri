def fibonacci_uret(adet: int):
    a, b = 0, 1
    for _ in range(adet):
        yield a
        a, b = b, a + b