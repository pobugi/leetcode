from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # to keep track if added value already seen in the array previously:
        window = set()

        # initialize left and right pointers:
        left = 0

        for right in range(len(nums)):
            # if window size exceed the limit, move left pointer:
            if right - left > k:
                window.remove(nums[left])
                left += 1
            # window size is ok and there is a duplicate
            if nums[right] in window:
                return True
            # else just add current number to the window
            window.add(nums[right])
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
