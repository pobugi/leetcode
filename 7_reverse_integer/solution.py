x = -12345


def get_number_digit(x):
    result = 0
    sign = 1
    if x < 0:
        x *= -1
        sign = -1
    while x:
        result *= 10
        result += x % 10
        x //= 10
    result = sign * result
    if result <= -2 ** 31 or result >= 2 ** 31 - 1:
        return 0

    return result


print(get_number_digit(x))
