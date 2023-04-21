def fib(n):
    cache = {0: 0, 1: 1}

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]


print(fib(2))  # 1
print(fib(3))  # 2
print(fib(4))  # 3
print(fib(8))  # 21
