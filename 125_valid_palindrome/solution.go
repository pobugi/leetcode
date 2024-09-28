package main

import (
	"fmt"
	"unicode"
)

func isPalindrome(s string) bool {
	var leftIndex, rightIndex int
	rightIndex = len(s) - 1

	for leftIndex < rightIndex {
		for leftIndex < rightIndex && !(unicode.IsLetter(rune(s[leftIndex])) || unicode.IsDigit(rune(s[leftIndex]))) {
			leftIndex++
		}
		for rightIndex > leftIndex && !(unicode.IsLetter(rune(s[rightIndex])) || unicode.IsDigit(rune(s[rightIndex]))) {
			rightIndex--
		}
		if unicode.ToLower(rune(s[leftIndex])) != unicode.ToLower(rune(s[rightIndex])) {
			return false
		}
		leftIndex++
		rightIndex--
	}
	return true
}

func main() {
	var s string
	s = "0P"
	fmt.Println(isPalindrome(s))
}
