from typing import List

strs = ["flower", "flow", "flight"]


def solve(strs: List[str]):
    # assign the first word as result
    res = list(strs[0])

    # to store temporary result
    temp_res = []
    for i in range(1, len(strs)):

        curr = strs[i]

        rng = min(len(res), len(curr))
        for j in range(rng):
            if curr[j] == res[j]:
                temp_res.append(curr[j])
            else:
                break

        # write the word of minimum length as a result
        if len(res) > len(temp_res):
            res = temp_res
        temp_res = []
    return "".join(res)


print(solve(strs))
