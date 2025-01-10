package main

import (
	"fmt"
	"math"
)

func minSubArrayLen(target int, nums []int) int {
	var left, right, currSum int
	var minLength = math.Inf(1)

	for left < len(nums) && right < len(nums) {
		for right < len(nums) && currSum < target {
			currSum += nums[right]
			right++
		}
		for left < right && currSum >= target {
			minLength = min(float64(right-left), minLength)
			currSum -= nums[left]
			left++
		}
	}
	if minLength == math.Inf(1) {
		return 0
	}
	return int(minLength)
}

func main() {
	var nums = []int{2, 3, 1, 2, 4, 3}
	var target int = 7

	fmt.Println(nums)
	fmt.Println(target)
	fmt.Println(minSubArrayLen(target, nums))
}
