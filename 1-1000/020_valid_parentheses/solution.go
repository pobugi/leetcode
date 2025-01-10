package main

import "fmt"

func isClosed(brace byte) bool {
	return brace == ')' || brace == '}' || brace == ']'
}

func isOpen(brace byte) bool {
	return brace == '(' || brace == '{' || brace == '['
}

func isMatching(brace1, brace2 byte) bool {
	return (brace1 == '(' && brace2 == ')') ||
		(brace1 == '{' && brace2 == '}') ||
		(brace1 == '[' && brace2 == ']')
}

func isValid(s string) bool {
	stack := []byte{}

	for i := 0; i < len(s); i++ {
		brace := s[i]
		if isOpen(brace) {
			stack = append(stack, brace)
		} else if isClosed(brace) {
			if len(stack) == 0 {
				return false
			}
			last := stack[len(stack)-1]
			if isMatching(last, brace) {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			return false
		}

	}
	return len(stack) == 0

}

func main() {
	fmt.Println(isValid("((()))"))
	fmt.Println(isValid("((())))"))
}
