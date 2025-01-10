package main

import "fmt"

func searchInsert(nums []int, target int) int {
	var start int = 0
	var end int = len(nums) - 1

	for start <= end {
		mid := (start + end) / 2
		if target == nums[mid] {
			return mid
		}
		if target > nums[mid] {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return start

}

func main() {
	fmt.Println(searchInsert([]int{1, 3, 5, 6}, 5))
}
