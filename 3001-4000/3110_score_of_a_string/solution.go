//class Solution:
//def scoreOfString(self, s: str) -> int:
//if len(s) <= 1:
//return 0
//result = 0
//for i in range(len(s) - 1):
//diff = abs(ord(s[i]) - ord(s[i + 1]))
//result += diff
//return diff
//
//
//s = Solution()
//print(s.scoreOfString("hello"))

package main

import (
	"fmt"
)

func abs(x int) int {
	if x < 0 {
		return -1 * x
	}
	return x
}

func scoreOfString(s string) int {
	if len(s) <= 1 {
		return 0
	}
	var result int
	for i := 0; i < len(s)-1; i++ {
		diff := abs(int(s[i]) - int(s[i+1]))
		result += diff
	}
	return result
}

func main() {
	fmt.Println(scoreOfString("hello"))
}
