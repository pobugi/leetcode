package main

func solve(matrix [][]int) {
	rows := make(map[int]bool)
	cols := make(map[int]bool)
	for rowIndex, row := range matrix {
		for colIndex, val := range row {
			if val == 0 {
				rows[rowIndex] = true
				cols[colIndex] = true
			}
		}
	}
	for rowIndex, row := range matrix {
		for colIndex, val := range row {
			if val != 0 {
				_, exists := rows[rowIndex]
				if exists {
					matrix[rowIndex][colIndex] = 0
				}
				_, exists = cols[colIndex]
				if exists {
					matrix[rowIndex][colIndex] = 0
				}
			}
		}
	}

}

func main() {
	var matrix = [][]int{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}
	solve(matrix)
}
