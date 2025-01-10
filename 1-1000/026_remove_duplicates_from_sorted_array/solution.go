package main

import (
	"fmt"
)

func removeDuplicates(nums []int) int {

	dict := make(map[int]bool)
	l := len(nums)
	i := 0

	for i < len(nums) {

		_, exists := dict[nums[i]]
		if exists {
			nums = append(nums[:i], nums[i+1:]...)
			l--
			i--
		}
		dict[nums[i]] = true
		i++
	}
	return len(nums)

}
func main() {
	var nums = []int{0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Println(removeDuplicates(nums))
}
