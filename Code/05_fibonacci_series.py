
def fibonacci_series(n):
    if n < 0:
        raise ValueError("Number must be non-negative")

    series = []
    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series