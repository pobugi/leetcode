# https://leetcode.com/problems/contains-duplicate/



def solve(nums):
    hash = {}
    
    for num in nums:
        if num in hash:
            return True
        hash[num] = 1
    return False


assert solve([1,2,3,1]) is True
assert solve([1,2,3,4]) is False
assert solve([1,1,1,3,3,4,3,2,4,2]) is True
print("success")
