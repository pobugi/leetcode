package main

import (
	"fmt"
	"strconv"
	"strings"
)

func convertDateToBinary(date string) string {
	var result []string
	for _, s := range strings.Split(date, "-") {
		number, _ := strconv.Atoi(s)
		binaryStr := strconv.FormatInt(int64(number), 2)
		result = append(result, binaryStr)
	}

	return strings.Join(result, "-")
}

func main() {
	fmt.Println(convertDateToBinary("2080-02-29"))
}
