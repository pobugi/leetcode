package main

import "fmt"

func finalValueAfterOperations(operations []string) int {
	var result int
	for i := 0; i < len(operations); i++ {
		switch operation := operations[i]; operation {
		case "++X":
			result++
		case "X++":
			result++
		case "--X":
			result--
		case "X--":
			result--
		}
	}
	return result
}

func main() {
	//operations := []string{"--X", "X++", "X++"}
	operations := []string{"++X", "++X", "X++"}
	fmt.Println(finalValueAfterOperations(operations))
}
