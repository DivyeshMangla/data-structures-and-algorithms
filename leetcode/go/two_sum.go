package main

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9

	for _, v := range twoSum(nums, target) {
		println(v)
	}
}

func twoSum(nums []int, target int) []int {
	appeared := make(map[int]int)

	for i1, num1 := range nums {
		needed := target - num1

		if i2, ok := appeared[needed]; ok && i1 != i2 {
			return []int{i1, i2}
		}

		appeared[num1] = i1
	}

	return []int{}
}
