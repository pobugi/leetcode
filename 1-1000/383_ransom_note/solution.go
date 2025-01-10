package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	dict := make(map[rune]int)
	for _, letter := range magazine {
		dict[letter]++
	}
	for _, r := range ransomNote {
		if dict[r] <= 0 {
			return false
		}
		dict[r]--
	}
	return true
}

func main() {
	fmt.Println(canConstruct("aaba", "aab"))
}
