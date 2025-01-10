# Recursive solution.

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


root = TreeNode(val=4)

left1 = TreeNode(val=2)
right1 = TreeNode(val=7)
root.left = left1
root.right = right1
left1.left = TreeNode(val=0)
left1.right = TreeNode(val=3)
right1.right = TreeNode(val=10)

TreeNode.print_node(root)
