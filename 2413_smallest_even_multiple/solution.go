package main

import "fmt"

func smallestEvenMultiple(n int) int {
	num := n
	for true {
		if num%n == 0 && num%2 == 0 {
			return num
		}
		num += n
	}
	return num
}

func main() {
	fmt.Println(smallestEvenMultiple(5))
	fmt.Println(smallestEvenMultiple(6))
}
