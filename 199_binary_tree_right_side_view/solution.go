package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	var result []int
	levels := make(map[int][]int)
	getLevels(root, levels, 0)
	for i := 0; i < len(levels); i++ {
		level := levels[i]
		if len(level) > 0 {
			result = append(result, level[len(level)-1])
		}
	}
	return result
}

func getLevels(root *TreeNode, levels map[int][]int, level int) {
	if root == nil {
		return
	}
	getLevels(root.Left, levels, level+1)
	levels[level] = append(levels[level], root.Val)
	getLevels(root.Right, levels, level+1)
}

func main() {
	root := TreeNode{
		Val:   1,
		Left:  &TreeNode{Val: 2, Right: &TreeNode{Val: 5}},
		Right: &TreeNode{Val: 3, Right: &TreeNode{Val: 4}},
	}
	fmt.Println(rightSideView(&root))
}
