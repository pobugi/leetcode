def gcd(num1: int, num2: int) -> int:

    while num1 and num2:

        if num1 > num2:
            num1, num2 = num2, num1
        num2 = num2 % num1

    return num1 or num2


print(gcd(24, 30))  # 6
print(gcd(17, 51))  # 17
print(gcd(24, 36))  # 12
print(gcd(24, 0))  # 24
print(gcd(24, -1))  # -1
