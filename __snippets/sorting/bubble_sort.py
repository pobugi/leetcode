from typing import List

arr = [5, 5, 15, -9, 1, 0, 8, -10, 0, -7, 14, -3]


def bubble_sort(nums: List[int]):
    n = len(nums)
    print("Initial array:")
    print(nums)
    print()

    for i in range(n):
        for j in range(i + 1, n):
            print(f"comparing {nums[i]} and {nums[j]} ...")
            if nums[i] > nums[j]:
                print(f"swappting {nums[i]} and {nums[j]} ...")
                nums[i], nums[j] = nums[j], nums[i]
            print(nums)
            print("-----------------------------")
        print("++++++++++++++++++++++++++++++")

    return nums


print(bubble_sort(arr))
