package main

import "fmt"

func isHappy(n int) bool {
	visited := make(map[int]bool)

	for !visited[n] {
		fmt.Println(visited)
		if n == 1 {
			return true
		}
		visited[n] = true
		n = getSumOfSquares(n)
	}
	return false
}

func getSumOfSquares(n int) int {
	var result int
	for n > 0 {
		reminder := n % 10
		result += reminder * reminder
		n /= 10
	}
	return result
}

func main() {
	fmt.Println(getSumOfSquares(19))
	fmt.Println(isHappy(19))
}
