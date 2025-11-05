package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var word string
		fmt.Scan(&word)
		fmt.Println(abbreviateWord(word))
	}
}

func abbreviateWord(word string) string {
	length := len(word)
	if length > 10 {
		return word[:1] + strconv.Itoa(length-2) + word[:length-1]
	}
	return word
}
