package main

import (
	"fmt"
	"sort"
)

func merge(intervals [][]int) [][]int {
	var result [][]int
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	result = append(result, intervals[0])

	for _, interval := range intervals[1:] {
		start, end := interval[0], interval[1]
		lastEnd := result[len(result)-1][1]
		if start <= lastEnd {
			result[len(result)-1][1] = max(lastEnd, end)
		} else {
			result = append(result, []int{start, end})
		}
	}

	return result
}

func main() {
	nums := [][]int{{2, 6}, {8, 10}, {15, 18}, {1, 3}}

	fmt.Println(merge(nums))
}
