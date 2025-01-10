nums = [-10, -3, 0, 5, 9]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


def arr_to_bst(nums: list):
    if not nums:
        return
    if len(nums) == 1:
        return Node(value=nums[0])
    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = arr_to_bst(nums[:mid])
    root.right = arr_to_bst(nums[mid + 1 :])
    return root


res = arr_to_bst(nums)
