arr = [7, 1, 5, 3, 6, 4]


def solve(arr):
    left = 0
    right = 1
    max_profit = 0

    while right < len(arr):
        # profitable?
        if arr[right] > arr[left]:
            profit = arr[right] - arr[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit


print(solve(arr))
