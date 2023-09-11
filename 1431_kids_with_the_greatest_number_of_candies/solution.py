candies = [2, 3, 5, 1, 3]
extra_candies = 3


def solve(candies: list, extra_candies: int):
    curr_max = max(candies)
    for i in range(len(candies)):
        candies[i] = True if candies[i] + extra_candies >= curr_max else False

    return candies


print(solve(candies, extra_candies))
