package main

func main() {
	s := "IV"
	print(romanToInt(s))
}

func romanToInt(s string) int {
	romanValue := map[rune]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	total := 0
	prev := 0

	for i := len(s) - 1; i >= 0; i-- {
		current := romanValue[rune(s[i])]

		if current < prev {
			total -= current
		} else {
			total += current
		}

		prev = current
	}

	return total
}
