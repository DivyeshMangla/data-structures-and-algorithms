package main

func majorityElement(nums []int) int {
	counts := make(map[int]int)
	for _, num := range nums {
		counts[num]++
	}

	majority := 0
	for num, count := range counts {
		if count > len(nums)/2 {
			majority = num
			break
		}
	}

	return majority
}
