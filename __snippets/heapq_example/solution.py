# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

import heapq

lst = [5, 7, 9, 1, 3]

heapq.heapify(lst)
print("The created heap is : ", (list(lst)))
