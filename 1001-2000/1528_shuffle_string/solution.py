class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = ["" for _ in range(len(s))]
        for index, value in zip(indices, s):
            result[index] = value
        return "".join(result)

s = Solution()
print(s.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))