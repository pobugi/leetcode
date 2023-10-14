def ways_to_climb_recursive(n):
    if n in (0, 1):
        return 1
    if n == 2:
        return 2

    return ways_to_climb(n - 1) + ways_to_climb(n - 2)


def ways_to_climb(n):
    cache = {0: 1, 1: 1, 2: 2}  # num: result

    if n in cache:
        return cache[n]
    cache[n] = ways_to_climb(n - 1) + ways_to_climb(n - 2)
    return cache[n]


print(ways_to_climb(1))
print(ways_to_climb(2))
print(ways_to_climb(3))
print(ways_to_climb(4))
print(ways_to_climb(5))
