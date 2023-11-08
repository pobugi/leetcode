matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

left, right = 0, len(matrix[0])
top, bottom = 0, len(matrix)

while left < right and top < bottom:
    "right:"
    for i in range(left, right):
        print(matrix[top][i], end=" ")
    top += 1
    "down:"
    for i in range(top, bottom):
        print(matrix[i][right - 1], end=" ")
    right -= 1
    "left:"
    for i in range(right - 1, left - 1, -1):
        print(matrix[bottom - 1][i], end=" ")
    bottom -= 1
    "up:"
    for i in range(bottom - 1, top - 1, -1):
        print(matrix[i][left], end=" ")
    left += 1
