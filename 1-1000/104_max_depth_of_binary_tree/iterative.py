class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def print_node(node):
        if not node:
            return
        TreeNode.print_node(node.left)
        print(node.val)
        TreeNode.print_node(node.right)

    @staticmethod
    def get_depth(node):
        if not node:
            return 0
        stack = [(node, 1)]
        max_depth = 1
        while stack:
            curr, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if curr.left:
                stack.append((curr.left, depth + 1))
            if curr.right:
                stack.append((curr.right, depth + 1))
        return max_depth


root = TreeNode(val=3)

left1 = TreeNode(val=9)
right1 = TreeNode(val=20)
root.left = left1
root.right = right1

right1.left = TreeNode(val=15)
right1.right = TreeNode(val=7)

right1.right.right = TreeNode(val=666)

TreeNode.print_node(root)
print("-----------")
print(TreeNode.get_depth(root))
