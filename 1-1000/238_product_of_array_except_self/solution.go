package main

import "fmt"

func main() {
	var nums = []int{1, 2, 3, 4}

	n := len(nums)
	result := make([]int, n)

	prefix := 1
	for i := 0; i < n; i++ {
		result[i] = prefix
		prefix *= nums[i]
	}
	fmt.Println(result)
	postfix := 1
	for i := n - 1; i >= 0; i-- {
		result[i] *= postfix
		postfix *= nums[i]
	}
	fmt.Println(result)
}
