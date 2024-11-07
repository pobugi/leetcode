package _26_invert_binary_tree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	curr := root
	if curr == nil {
		return nil
	}
	curr.Left, curr.Right = curr.Right, curr.Left
	invertTree(curr.Left)
	invertTree(curr.Right)
	return root
}

func main() {

}
