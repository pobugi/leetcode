package main

import (
	"fmt"
)

func majorityElement2(nums []int) int {
	dict := make(map[int]int)
	for _, value := range nums {
		dict[value]++
	}
	var maxValue, result int
	for key, value := range dict {
		if value > maxValue {
			result = key
			maxValue = value
		}
	}
	return result
}

func main() {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	fmt.Println(majorityElement2(nums))
}
