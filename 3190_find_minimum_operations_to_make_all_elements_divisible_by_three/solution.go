package main

import "fmt"

func minimumOperations(nums []int) int {
	var result int
	for _, val := range nums {
		sr := GetMinStepsToMakeDivisibleBy3(val)
		fmt.Println(sr)
		result += sr
	}
	return result
}

func IsDivisibleBy3(num int) bool {
	if num%3 == 0 {
		return true
	}
	return false
}

func GetMinStepsToMakeDivisibleBy3(num int) int {
	if IsDivisibleBy3(num) {
		return 0
	}
	var leftResult, rightResult int
	for i := num; true; i++ {
		if IsDivisibleBy3(i) {
			rightResult = i - num
			break
		}
	}
	for i := num; true; i-- {
		if IsDivisibleBy3(i) {
			leftResult = num - i
			break
		}
	}
	return min(leftResult, rightResult)
}

func main() {
	nums := []int{8}
	fmt.Println(minimumOperations(nums))
}
