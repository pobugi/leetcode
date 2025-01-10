import heapq
from collections import defaultdict
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flat = [self.ll_to_list(lst) for lst in lists]
        merged = self.merge(flat)
        return self.list_to_ll(merged)

    def merge(self, lists: list[list[int]]) -> list[int]:
        hash = defaultdict(int)
        result = []

        for lst in lists:
            for num in lst:
                hash[num] += 1
        keys = list(hash.keys())
        heapq.heapify(keys)

        while keys:
            key = heapq.heappop(keys)
            for _ in range(hash[key]):
                result.append(key)

        return result

    def ll_to_list(self, root: ListNode) -> list:
        res = []
        if not root:
            return res
        while root:
            if isinstance(root, ListNode):
                res.append(root.val)
                root = root.next
            else:
                return res
        return res

    def list_to_ll(self, lst):
        root = ListNode(0)
        curr = root
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return root.next
