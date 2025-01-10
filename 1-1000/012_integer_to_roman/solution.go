package main

import "fmt"

func intToRoman(num int) string {
	var result string
	ones := []string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
	tens := []string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
	hundreds := []string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
	thousands := []string{"", "M", "MM", "MMM"}

	i1 := num % 10
	i10 := num % 100 / 10
	i100 := num % 1000 / 100
	i1000 := num % 10000 / 1000

	result = thousands[i1000] + hundreds[i100] + tens[i10] + ones[i1]
	return result
}

func main() {
	fmt.Println(intToRoman(1999))
}
