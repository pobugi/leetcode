def power(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        return 1 / power(x, -n)

    if n % 2 == 0:
        part = power(x, n // 2)
        return part * part
    if n % 3 == 0:
        part = power(x, n // 3)
        return part * part * part
    return x * power(x, n - 1)


print(power(x=2.00000, n=-2))
print(power(x=2.00000, n=0))
print(power(x=2.00000, n=1))
print(power(x=2.00000, n=2))
print(power(x=2.00000, n=3))
print(power(x=2.00000, n=4))
