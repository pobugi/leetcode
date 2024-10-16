package main

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int) // value : index

	for index, num := range nums {
		valueRequired := target - num
		_, exists := dict[valueRequired]
		if exists {
			return []int{num, valueRequired}
		}
		dict[num] = index
	}
	return []int{}
}

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	var result [][]int
	var left, right int

	for i, num := range nums {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		left = i + 1
		right = len(nums) - 1

		for left < right {
			summa := num + nums[left] + nums[right]
			if summa == 0 {
				result = append(result, []int{num, nums[left], nums[right]})
				left++
				for nums[left] == nums[left-1] && left < right {
					left++
				}
			} else if summa > 0 {
				right--
			} else {
				left++
			}
		}
	}
	return result
}

func main() {
	var nums = []int{-1, 0, 1, 2, -1, -4, -4}
	fmt.Println(threeSum(nums))
}
