package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	firstStr := strs[0]
	for _, secondStr := range strs[1:] {
		var i, j int
		for i < len(firstStr) && j < len(secondStr) && firstStr[i] == secondStr[j] {
			i++
			j++
		}
		firstStr = firstStr[:i]
	}
	return firstStr
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(strs))
}
