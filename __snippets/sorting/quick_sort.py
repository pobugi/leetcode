def quick_sort(arr: list):
    print(f"call quick_sort for arr: {arr}")
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    gt_than_pivot = [num for num in arr[1:] if num > pivot]
    lte_than_pivot = [num for num in arr[1:] if num <= pivot]
    print(lte_than_pivot, pivot, gt_than_pivot)
    result = quick_sort(lte_than_pivot) + [pivot] + quick_sort(gt_than_pivot)
    print(result)
    return result

arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))