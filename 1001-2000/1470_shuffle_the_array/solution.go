package main

import "fmt"

func shuffle(nums []int, n int) []int {
	var arr []int
	for i := 0; i < n; i++ {
		arr = append(arr, nums[i])
		arr = append(arr, nums[i+n])
	}
	return arr
}

func main() {
	arr := []int{2, 5, 1, 3, 4, 7}
	result := shuffle(arr, 3)
	fmt.Println(result)
}
