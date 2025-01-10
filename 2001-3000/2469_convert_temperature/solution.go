package main

import (
	"fmt"
	"math"
)

func roundToTwoDecimals(x float64) float64 {
	return math.Round(x)
}

func convertTemperature(celsius float64) []float64 {
	kelvin := roundToTwoDecimals(celsius + 273.15)
	fahrenheit := roundToTwoDecimals(celsius*1.80 + 32.00)
	result := []float64{kelvin, fahrenheit}
	return result
}

func main() {
	fmt.Println(convertTemperature(122.11))
}
