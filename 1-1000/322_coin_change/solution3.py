coins = [1, 3, 4, 5]
target = 7


def coin_change(coins: list[int], target: int):
    result = []
    coins.sort(reverse=True)

    def dfs(target, coins_set):
        if target < 0:
            return
        if target == 0:
            result.append(coins_set.copy())
            return
        for coin in coins:
            mult = target // coin
            if mult == 0:
                continue
            cns = [coin] * mult
            coins_set.extend(cns)
            dfs(target - coin * mult, coins_set)
            for _ in range(mult):
                coins_set.pop()

    dfs(target, [])
    return result


print(coin_change([1, 3, 4, 5], 7))
# print(coin_change([1, 2, 5], 100))
