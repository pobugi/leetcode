def solve(n):
    result = []
    for i in range(2, int(n**0.5)):
        # if n == 1:
        #     break
        while n % i == 0 and n != 1:
            result.append(i)
            n //= i
    if n:
        result.append(n)
    return result


print(solve(21))
