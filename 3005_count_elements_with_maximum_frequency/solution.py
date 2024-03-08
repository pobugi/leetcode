class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        hash = dict()
        max_freq = 0
        for num in nums:
            curr_freq = hash.get(num, 0) + 1
            max_freq = max(max_freq, curr_freq)
            hash[num] = curr_freq

        res = 0
        for key in hash.keys():
            if hash[key] == max_freq:
                res += max_freq
        return res


s = Solution()
print(s.maxFrequencyElements([1, 2, 3, 4]))
print(s.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
