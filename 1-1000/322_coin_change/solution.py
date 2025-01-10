coins = [1, 2, 5]
amount = 11

# 3: 11 = 5 + 5 + 1


def coin_change(amount: int, coins: list[int]):
    coins.sort(reverse=True)
    result = 0
    for coin in coins:
        possible_amount = amount // coin
        if possible_amount > 0:
            result += possible_amount
            print(f"{coin} x {possible_amount} = {coin * possible_amount}")
            amount -= possible_amount * coin
    if amount > 0:
        return -1
    return result


class Node:
    def __init__(self, value: int, coins: list[int]):
        self.value = value
        # self.multiplier = 0
        self.coins = coins
        self.children: list[Node] = []

    def __repr__(self):
        return str(self.value) or None


def build_tree(root: Node | None, coins: list[int]):
    if not root:
        return root
    if root.value <= 0:
        return root
    if root.value < min(coins):
        return root
    for coin in coins:
        val = root.value
        possible_amount = val // coin
        remainder = val - coin * possible_amount
        if remainder <= 0:
            continue
        child = Node(remainder, coins)
        root.children.append(child)

        x = 7
        # value = root.value
        # while value > coin and value > 0:
        #     value -= coin
        #     if coin > value:
        #         break
        #     child = Node(value - coin, coins)
        #     root.children.append(child)
    for child in root.children:
        build_tree(child, coins)
    return root


# root = Node(value=6249, coins=[419, 408, 186, 83])
# build_tree(root, [419, 408, 186, 83])

root = Node(value=11, coins=[5, 2, 1])
build_tree(root, [5, 2, 1])

66
# print(coin_change(amount, coins))
# print(coin_change(3, [2]))
# print(coin_change(0, [1]))
# print(coin_change(6249, [186, 419, 83, 408]))
