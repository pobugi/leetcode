num = 123
result = 0

while num:
    result *= 10
    result += num % 10
    num //= 10

print(result)