package main

import (
	"fmt"
)

func strStr(haystack string, needle string) int {
	var i, j, k int

	for k < len(haystack) {
		for i < len(haystack) && j < len(needle) && haystack[i] == needle[j] {
			i++
			j++
		}
		if i-k == len(needle) {
			return k
		}
		k++
		i = k
		j = 0

	}
	return -1

}
func main() {
	var haystack, needle string
	haystack = "sadbutsad"
	needle = "sad"
	fmt.Println(strStr(haystack, needle))
}
