package main

import "fmt"

func isSubsequence(s string, t string) bool {

	var j, total int
	total = len(s)

	for _, letter := range s {
		for j < len(t) && rune(letter) != rune(t[j]) {
			j++
		}
		if j < len(t) && rune(letter) == rune(t[j]) {
			total--
			j++
		}
	}
	return total == 0
}

func main() {

	fmt.Println(isSubsequence("abcw", "ahbgdcw"))
	fmt.Println(isSubsequence("abcwt", "ahbgdcw"))

}
