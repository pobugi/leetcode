#  https://leetcode.com/problems/jewels-and-stones/description/

jewels = "aA"
stones = "aAAbbbb"


def solve(jewels, stones):
    hash_map = dict()
    for stone in stones:
        hash_map[stone] = 1 + hash_map.get(stone, 0)
    return sum(hash_map.get(letter, 0) for letter in jewels)


print(solve(jewels, stones))
