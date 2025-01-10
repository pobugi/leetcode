package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	values := []int{}
	dfs(root, &values)
	root.Left = nil
	if len(values) <= 1 {
		return
	}
	for i := 1; i < len(values); i++ {
		root.Right = &TreeNode{Val: values[i]}
		root.Left = nil
		root = root.Right
	}
}

func dfs(root *TreeNode, values *[]int) {
	if root == nil {
		return
	}
	*values = append(*values, root.Val)
	dfs(root.Left, values)
	dfs(root.Right, values)
}

func main() {
	values := []int{}
	tree1 := TreeNode{
		Val:   1,
		Left:  &TreeNode{Val: 2, Left: &TreeNode{Val: 3}, Right: &TreeNode{Val: 4}},
		Right: &TreeNode{Val: 5, Right: &TreeNode{Val: 6}},
	}
	fmt.Println(values)
	dfs(&tree1, &values)
	fmt.Println(values)
}
