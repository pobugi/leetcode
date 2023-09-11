
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
        return 1 + max(TreeNode.get_depth(node.left), TreeNode.get_depth(node.right))


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
