package main

import "fmt"

func IsOpenBracket(bracket string) bool {
	if bracket == "(" || bracket == "{" || bracket == "[" {
		return true
	}
	return false
}

func IsClosingBracket(bracket string) bool {
	if bracket == ")" || bracket == "}" || bracket == "]" {
		return true
	}
	return false
}

func MatchingBracket(openBracket string, closingBracket string) bool {
	if openBracket == "(" && closingBracket == ")" {
		return true
	}
	if openBracket == "{" && closingBracket == "}" {
		return true
	}
	if openBracket == "[" && closingBracket == "]" {
		return true
	}
	return false
}

func solve(brackets string) bool {
	var stack []string
	for _, char := range brackets {
		bracket := string(char)
		if IsOpenBracket(bracket) {
			stack = append(stack, bracket)
		} else if IsClosingBracket(bracket) {
			if len(stack) > 0 {
				lastBracket := stack[len(stack)-1]
				if MatchingBracket(lastBracket, bracket) {
					stack = stack[:len(stack)-1]
				} else {
					return false
				}

			} else {
				return false
			}
		}

	}
	if len(stack) > 0 {
		return false
	}
	return true

}

func main() {
	brackets := "()[]{}"
	fmt.Println(solve(brackets))
}
