package main

import "fmt"

func ArrPop(arr *[]int, index int) {
	*arr = append((*arr)[:index], (*arr)[index+1:]...)
}

func removeElement(nums []int, val int) int {

	l := len(nums)
	i := 0
	for i < l {
		if nums[i] == val {
			ArrPop(&nums, i)
			l--
		} else {
			i++
		}
	}
	return len(nums)
}

func main() {
	//var arr = []int{0, 1, 2, 2, 3, 0, 4, 2}
	var arr = []int{3, 2, 2, 3}

	fmt.Println(removeElement(arr, 3))

}
