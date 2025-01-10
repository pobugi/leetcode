package main

import "fmt"

func isAnagram(s string, t string) bool {
	dict := make(map[rune]int)

	for _, char := range s {
		dict[char]++
	}
	for _, char := range t {
		dict[char]--
	}
	for _, val := range dict {
		if val != 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}
