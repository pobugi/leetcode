# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


def brute_force(temperatures: list[int]) -> list[int]:
    result = []
    for i in range(len(temperatures)):
        j = i
        days = 0
        while j < len(temperatures) and temperatures[j] <= temperatures[i]:
            days += 1
            j += 1
        if j < len(temperatures) and temperatures[j] > temperatures[i]:
            result.append(days)
        else:
            result.append(0)

    return result


print(brute_force([73, 74, 75, 71, 69, 72, 76, 73]))
