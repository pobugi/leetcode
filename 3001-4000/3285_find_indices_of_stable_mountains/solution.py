from typing import List


class Solution:
	def stableMountains(self, height: List[int], threshold: int) -> List[int]:
		result = []
		for i in range(1, len(height)):
			if height[i-1] > threshold:
				result.append(i)
		return result


s = Solution()
print(s.stableMountains(height=[1, 2, 3, 4, 5], threshold=2))