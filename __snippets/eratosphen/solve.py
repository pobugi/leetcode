# разложение числа на простые множители


def eratosphen(n: int):
    result = []

    curr_num = 2
    while curr_num * curr_num <= n:
        if n % curr_num == 0:
            result.append(curr_num)
            n //= curr_num
        else:
            curr_num += 1
    if n > 1:
        result.append(n)

    return result


print(eratosphen(2971))
