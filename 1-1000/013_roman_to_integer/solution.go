package main

import "fmt"

func romanToInt(s string) int {
	symbols := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	var result int
	for i := len(s) - 1; i >= 0; i-- {
		if i < len(s)-1 && symbols[string(s[i+1])] > symbols[string(s[i])] {
			result -= symbols[string(s[i])]
		} else {
			result += symbols[string(s[i])]
		}
	}
	return result
}

func main() {
	fmt.Println(romanToInt("VIII"))
}
