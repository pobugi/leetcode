from dataclasses import dataclass

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@dataclass
class Point:
    row: int
    col: int


def go_right(matrix, src: Point, dst: Point):
    while src.col <= dst.col:
        print(matrix[src.row][src.col], end=" ")
        src.col += 1


def go_down(matrix, src: Point, dst: Point):
    while src.row <= dst.row:
        print(matrix[src.row][src.col], end=" ")
        src.row += 1


def go_left(matrix, src: Point, dst: Point):
    while src.col >= dst.col:
        print(matrix[src.row][src.col], end=" ")
        src.col -= 1


def go_up(matrix, src: Point, dst: Point):
    while src.row >= dst.row:
        print(matrix[src.row][src.col], end=" ")
        src.row -= 1


def spiral(
    matrix: list[list[int]],
    top_left: Point,
    top_right: Point,
    bottom_left: Point,
    bottom_right: Point,
):
    # print(f"call for {top_left} {top_right} {bottom_right} {bottom_left}")
    go_right(matrix, src=top_left, dst=top_right)
    top_left.row += 1
    top_right.row += 1
    go_down(matrix, src=top_right, dst=bottom_right)
    bottom_right.col -= 1
    go_left(matrix, src=bottom_right, dst=bottom_left)
    bottom_left.row -= 1
    go_up(matrix, src=bottom_left, dst=top_left)


def solve(matrix: list[list[int]]):
    # number of cycles:
    rows = len(matrix)
    cycles = rows // 2 + 1 if rows % 2 else rows // 2

    tl = [0, 0]
    tr = [0, rows - 1]
    bl = [rows - 1, 0]
    br = [rows - 1, rows - 1]

    for i in range(cycles):
        top_left = Point(tl[0], tl[1])
        top_right = Point(tr[0], tr[1])
        bottom_left = Point(bl[0], bl[1])
        bottom_right = Point(br[0], br[1])

        spiral(matrix, top_left, top_right, bottom_left, bottom_right)
        tl[0] += 1
        tl[1] += 1
        tr[0] += 1
        tr[1] -= 1
        bl[0] -= 1
        bl[1] += 1
        br[0] -= 1
        br[1] -= 1


solve(matrix)
