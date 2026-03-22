package main

func titleToNumber(columnTitle string) int {
	result := 0

	for _, char := range columnTitle {
		charValue := int(char - 'A' + 1)
		result = result*26 + charValue
	}

	return result
}
