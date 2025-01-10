package main

import (
	"fmt"
	"strings"
)

func solve(path string) string {
	var stack []string
	var curr, letter string

	for _, rn := range path + "/" {
		letter = string(rn)
		if letter == "/" {
			if curr == ".." {
				if len(stack) > 0 {
					stack = stack[:len(stack)-1]
				}
			} else if curr != "" && curr != "." {
				stack = append(stack, curr)
			}
			curr = ""
		} else {
			curr += letter
		}
	}

	return "/" + strings.Join(stack, "/")
}

func main() {
	fmt.Println(solve("/../abc/./def/"))
	fmt.Println(solve("/home/user/Documents/../Pictures"))
}
