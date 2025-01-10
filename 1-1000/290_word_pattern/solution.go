package main

import (
	"fmt"
	"strings"
)

func wordPattern(pattern string, s string) bool {

	words := strings.Split(s, " ")

	if len(words) != len(pattern) {
		return false
	}
	charToWord := make(map[int32]string)
	wordToChar := make(map[string]int32)
	for index, char := range pattern {

		value, exists := charToWord[char]
		if exists && value != words[index] {
			return false
		}
		v, e := wordToChar[words[index]]
		if e && v != char {
			return false
		}
		charToWord[char] = words[index]
		wordToChar[words[index]] = char
	}
	return true
}

func main() {
	pattern := "abba"
	s := "dog cat cat dog"
	//s := "dog dog dog dog"
	fmt.Println(wordPattern(pattern, s))
}
