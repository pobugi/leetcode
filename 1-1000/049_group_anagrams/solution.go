package main

import (
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	result := make(map[string][]string)
	var output [][]string
	for _, s := range strs {
		key := sortString(s)
		result[key] = append(result[key], s)
	}

	for _, group := range result {
		output = append(output, group)
	}

	return output
}

func sortString(s string) string {
	strArr := strings.Split(s, "")
	sort.Strings(strArr)
	return strings.Join(strArr, "")
}

func main() {
	var strs = []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(groupAnagrams(strs))
}

/*
def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = {}

    for s in strs:
        letters = {letter: 0 for letter in ALPHABET}
        for letter in s:
            letters[letter] += 1
        key = tuple(letters.values())
        if key in result:
            result[key].append(s)
        else:
            result[key] = [s]

    return list(result.values())
*/
