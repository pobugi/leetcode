package main

import (
	"fmt"
	"math"
)

func assertInt32(value interface{}) (int, bool) {
	// Используем type assertion
	if v, ok := value.(int); ok {
		return v, true
	}
	return 0, false
}

func isInt32(value int) bool {
	return value >= math.MinInt32 && value <= math.MaxInt32
}

func reverse(x int) int {

	var result int
	var sign = 1

	if x < 0 {
		x *= -1
		sign = -1
	}

	for x > 0 {
		digit := x % 10
		x /= 10
		result *= 10
		result += digit
	}
	result *= sign

	ok := isInt32(result)
	if ok {
		return result
	}
	return 0
}

func main() {
	var num = -12345

	fmt.Println(num)
}
