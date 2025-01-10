package main

import "fmt"

func maxProfit(prices []int) int {
	var maxProfit int
	var buyIndex int
	var sellIndex int

	for sellIndex < len(prices) {
		if prices[sellIndex] > prices[buyIndex] {
			currProfit := prices[sellIndex] - prices[buyIndex]
			maxProfit = max(currProfit, maxProfit)
		} else {
			buyIndex = sellIndex
		}
		sellIndex++
	}
	return maxProfit
}

func main() {
	fmt.Println(maxProfit([]int{7, 1, 5, 3, 6, 4}))
}
