class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        occurrences = {}
        for item in arr:
            occurrences[item] = occurrences.get(item, 0) + 1

        # Sort the list based on the sorting key
        sorted_list = sorted(arr, key=lambda item: (occurrences[item], item))

        return len(set(sorted_list[k:]))
