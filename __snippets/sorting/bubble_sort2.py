def bubble_sort(arr: list):

    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            print("------------------")
            print(arr)
            print(f"curr: {arr[j]}")
            print(f"compare {arr[j]} with {arr[j + 1]}:")
            if arr[j] > arr[j + 1]:
                print(f"swap {arr[j]} and {arr[j + 1]}:")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
