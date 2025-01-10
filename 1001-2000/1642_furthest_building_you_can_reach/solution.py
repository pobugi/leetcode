# heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
# bricks = 10
# ladders = 2

heights = [1, 5, 1, 2, 3, 4, 1000]
bricks = 4
ladders = 1


class Node:
    def __init__(
        self,
        curr: int,
        bricks: int,
        ladders: int,
        arr: list | None = None,
        left: "Node | None" = None,
        mid: "Node | None" = None,
        right: "Node | None" = None,
    ) -> None:
        self.curr = curr
        self.bricks = bricks
        self.ladders = ladders
        self.left = left
        self.mid = mid
        self.right = right
        self.arr = arr

    def __repr__(self) -> str:
        return f"Node: {self.curr}, bricks: {self.bricks}, ladders: {self.ladders}, arr: {self.arr}"

    def __str__(self) -> str:
        return f"Node: {self.curr}, bricks: {self.bricks}, ladders: {self.ladders}, arr: {self.arr}"


root = Node(curr=heights[0], arr=heights[1:], bricks=bricks, ladders=ladders)
# left - bricks
# mid - ladders
# right - None

# diff = root.arr[0] - root.curr
# root.left = Node(curr=root.arr[0], arr=root.arr[1:], bricks=root.bricks - diff, ladders=root.ladders)


def solve(root: Node | None):
    if not root:
        return 0
    if not root.arr:
        return 0
    diff = root.arr[0] - root.curr
    print(root)
    if root.arr[0] <= root.curr:
        root.right = Node(curr=root.arr[0], arr=root.arr[1:], bricks=root.bricks, ladders=root.ladders)
        solve(root.right)

    if root.bricks >= diff and root.arr[0] > root.curr:
        print(f"{root.bricks} - {diff} = {root.bricks - diff}")
        root.left = Node(curr=root.arr[0], arr=root.arr[1:], bricks=root.bricks - diff, ladders=root.ladders)
        solve(root.left)
    if root.ladders > 0 and root.arr[0] > root.curr:
        root.mid = Node(curr=root.arr[0], arr=root.arr[1:], bricks=root.bricks, ladders=root.ladders - 1)
        solve(root.mid)


solve(root)


def get_depth(root: Node | None) -> int:
    if not root:
        return 0
    return 1 + max(get_depth(root.left), get_depth(root.right), get_depth(root.mid))


print(get_depth(root))

44
assert True
