arr = [0, 5, 77, 7, 8, 8, 10, 1, 4, 1]

for i in range(len(arr)):
    for j in range(i, len(arr) + 1):
        print(arr[j:])

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)

    return arr


# bubble_sort(arr)
# print(arr)