package main

import (
	"fmt"
	"strings"
)

func rev(s string) string {
	var i int
	var resultSlice []string
	var subStr string

	for i < len(s) {
		for i < len(s) && string(s[i]) == " " {
			i++
		}
		for i < len(s) && string(s[i]) != " " {
			subStr = subStr + string(s[i])
			i++
		}
		if subStr != "" {
			resultSlice = append([]string{subStr}, resultSlice...)
		}
		subStr = ""
	}
	result := strings.Join(resultSlice, " ")
	return result

}
func main() {
	s := "the sky is blue"
	fmt.Println(rev(s))
}
