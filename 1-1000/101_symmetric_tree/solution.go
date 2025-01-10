package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	return compare(root.Left, root.Right)
}

func compare(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == nil && root2 == nil {
		return true
	}
	if (root1 == nil && root2 != nil) || (root1 != nil && root2 == nil) {
		return false
	}
	if root1.Val != root2.Val {
		return false
	}
	return compare(root1.Right, root2.Left) && compare(root1.Left, root2.Right)
}

func main() {

}
