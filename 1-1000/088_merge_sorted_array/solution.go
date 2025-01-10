package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) int {
	lastIndex := m + n - 1

	for m > 0 && n > 0 {
		if nums1[m-1] > nums2[n-1] {
			nums1[lastIndex] = nums1[m-1]
			m--
		} else {
			nums1[lastIndex] = nums2[n-1]
			n--
		}
		lastIndex--
	}
	for n > 0 {
		nums1[lastIndex] = nums2[n-1]
		n--
		lastIndex--
	}
	fmt.Println(nums1, nums2)
	return 0

}

func main() {
	nums1 := []int{1, 4, 8, 0, 0, 0}
	m := 3
	nums2 := []int{2, 5, 6}
	n := 3
	fmt.Println(merge(nums1, m, nums2, n))
}
