package main

import "fmt"

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int) // value : index

	for index, num := range nums {
		valueRequired := target - num
		_, exists := dict[valueRequired]
		if exists {
			return []int{index, dict[valueRequired]}
		}
		dict[num] = index
	}
	fmt.Println(dict)
	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	fmt.Println(twoSum(nums, 9))
}
