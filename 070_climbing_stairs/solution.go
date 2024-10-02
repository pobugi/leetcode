package main

import "fmt"

func climbStairs(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	first := 1
	second := 2
	for i := 3; i <= n; i++ {
		first, second = second, first+second
	}
	return second
}

func main() {
	fmt.Println(climbStairs(300))
}
