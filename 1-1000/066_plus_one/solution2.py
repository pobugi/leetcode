def solve(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        curr = digits[i] + carry
        if curr < 10:
            digits[i] = curr
            carry = 0
        else:
            digits[i] = 0
            carry = 1
    if carry:
        digits = [1] + digits
    return digits


print(solve([4, 3, 2, 1]))
print(solve([9, 9, 0]))
