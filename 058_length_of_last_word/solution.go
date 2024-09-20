package main

import "fmt"

func lengthOfLastWord(s string) int {
	var currLen, lastLen, left, right int

	for right < len(s) && left < len(s) {
		lastLen = currLen
		currLen = 0
		for right < len(s) && string(s[right]) == " " {
			right++
			left++
		}
		for right < len(s) && string(s[right]) != " " {
			currLen++
			right++
		}
		currLen = right - left
		left = right
	}
	if currLen > 0 {
		return currLen
	}
	return lastLen
}

func main() {
	fmt.Println(lengthOfLastWord("Hello World"))
}
