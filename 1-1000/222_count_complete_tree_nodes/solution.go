package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getTreeSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return root.Val + getTreeSum(root.Left) + getTreeSum(root.Right)
}

func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func main() {
	root := TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val:   2,
			Left:  &TreeNode{Val: 4},
			Right: &TreeNode{Val: 5},
		},
		Right: &TreeNode{
			Val:  3,
			Left: &TreeNode{Val: 6},
		},
	}
	fmt.Println(countNodes(&root))
	fmt.Println(getTreeSum(&root))
}
