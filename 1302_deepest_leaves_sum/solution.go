package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deepestLeavesSum(root *TreeNode, levels map[int][]int, level int) {
	if root == nil {
		return
	}
	deepestLeavesSum(root.Left, levels, level+1)
	levels[level] = append(levels[level], root.Val)
	deepestLeavesSum(root.Right, levels, level+1)
}

func main() {
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val:  4,
				Left: &TreeNode{Val: 7},
			},
			Right: &TreeNode{
				Val: 5,
			},
		},
		Right: &TreeNode{
			Val: 3,
			Right: &TreeNode{
				Val:   6,
				Right: &TreeNode{Val: 8},
			},
		},
	}

	levels := make(map[int][]int)
	deepestLeavesSum(root, levels, 0)
	fmt.Println(levels)

	var maxLevel, result int

	for key, _ := range levels {
		maxLevel = max(key, maxLevel)
	}
	for _, value := range levels[maxLevel] {
		result += value
	}
	fmt.Println(result)

}
