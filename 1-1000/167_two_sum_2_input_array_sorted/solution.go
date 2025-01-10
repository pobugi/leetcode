package main

import "fmt"

func binarySearch(arr []int, target int, start int) int {
	var mid int
	end := len(arr) - 1
	for start <= end {
		mid = (start + end) / 2
		if arr[mid] == target {
			return mid
		}
		if arr[mid] > target {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return -1
}

func twoSum(numbers []int, target int) []int {
	for index, value := range numbers {
		searchTarget := target - value
		result := binarySearch(numbers, searchTarget, index+1)
		if result > -1 {
			return []int{index + 1, result + 1}
		}
	}
	return []int{-1, -1}
}

func main() {

	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))

}
