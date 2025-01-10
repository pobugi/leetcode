"""
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Input: time = "0?:3?"
Output: "09:39"

Input: time = "1?:22"
Output: "19:22"
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2, s, m1, m2 = list(time)
        if h1.isdigit():
            h1 = int(h1)
        if h2.isdigit():
            h2 = int(h2)
        if m1.isdigit():
            m1 = int(m1)
        if m2.isdigit():
            m2 = int(m2)
        if h1 == "?":
            if isinstance(h2, int) and h2 > 3:
                h1 = 1
            else:
                h1 = 2
        if h2 == "?":
            if h1 in (0, 1):
                h2 = 9
            elif h1 == 2:
                h2 = 3
        if m1 == "?":
            if m2 in ("?", 0):
                m1 = 5
            else:
                m1 = 5
        if m2 == "?":
            if m1 in (1, 2, 3, 4, 5):
                m2 = 9
            elif m1 == 6:
                m2 = 6
            elif m1 == 0:
                m2 = 9
        return f"{h1}{h2}:{m1}{m2}"


print(Solution().maximumTime("2?:?0"))
print(Solution().maximumTime("?4:03"))
