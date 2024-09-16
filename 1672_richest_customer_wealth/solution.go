package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	var maxWealth int

	for i := 0; i < len(accounts); i++ {
		var currWealth int
		for j := 0; j < len(accounts[i]); j++ {
			currWealth += accounts[i][j]
		}
		maxWealth = max(maxWealth, currWealth)
	}
	return maxWealth
}

func main() {
	// Define the 2D slice accounts
	accounts := [][]int{
		{1, 2, 3},
		{3, 2, 1},
	}
	result := maximumWealth(accounts)
	fmt.Println("Maximum Wealth:", result)
}
