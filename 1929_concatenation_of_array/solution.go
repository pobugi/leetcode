package main

import "fmt"

func main() {
	nums := []int{1, 3, 2, 1}
	fmt.Println(nums)
	nums = append(nums, nums...)
	fmt.Println(nums)
}
