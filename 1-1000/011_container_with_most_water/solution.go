package main

import "fmt"

func maxArea(height []int) int {
	var left, right, res, curr int
	right = len(height) - 1

	for left < right {
		curr = min(height[right], height[left]) * (right - left)
		res = max(curr, res)
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return res
}
func main() {
	var height []int
	height = []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(height))
}
