package main

import (
	"strconv"
)

func main() {
	number := 10
	println(isPalindrome(number))
}

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	str := strconv.Itoa(x)
	chars := []rune(str)
	length := len(chars)
	checkTill := length / 2

	for i := 0; i < checkTill; i++ {
		if chars[i] != chars[length-i-1] {
			return false
		}
	}

	return true
}
