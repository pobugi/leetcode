package main

import "fmt"

func plusOne(digits []int) []int {
	var carry int = 1
	for i := len(digits) - 1; i >= 0; i-- {
		curr := digits[i] + carry
		if curr < 10 {
			digits[i] = curr
			carry = 0
		} else {
			digits[i] = 0
			carry = 1
		}
	}
	if carry > 0 {
		digits = append([]int{1}, digits...)
	}
	return digits
}

func main() {
	fmt.Println(plusOne([]int{4, 3, 2, 1}))
	fmt.Println(plusOne([]int{9, 9, 9}))
	fmt.Println(plusOne([]int{9, 9, 8}))
	fmt.Println(plusOne([]int{9}))
}
