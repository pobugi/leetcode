"""Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5.
The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or
more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12."""

nums = [1, 12, 1, 2, 5, 50, 3]


def solve(nums):
    # sort array in reverse order
    nums.sort(reverse=True)
    # get summ of all numbers
    summa = sum(nums)
    for num in nums:
        # sum of other values:
        summa = summa - num
        # if current num is less than others sum
        # that means that polygon is valid
        if num < summa:
            return summa + num
    return -1


print(solve(nums))
