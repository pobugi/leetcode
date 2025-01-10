package main

func countConsistentStrings(allowed string, words []string) int {

	allowedMap := make(map[rune]bool)
	var result int

	for _, char := range allowed {
		allowedMap[char] = true
	}

	for _, word := range words {

		isConsistent := true

		for _, char := range word {
			if !allowedMap[char] {
				isConsistent = false
				break
			}
		}
		if isConsistent {
			result++
		}

	}
	return result

}

func main() {
	return
}
