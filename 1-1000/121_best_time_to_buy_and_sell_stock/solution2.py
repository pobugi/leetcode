prices = [7, 1, 5, 3, 6, 4]


def solve(prices: list[int]):
    max_profit = 0
    buy = 0  # index
    sell = 1  # index

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            curr_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, curr_profit)
        else:
            buy = sell
        sell += 1

    return max_profit


print(solve(prices))
