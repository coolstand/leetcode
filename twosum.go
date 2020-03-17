package main

import (
	"fmt"
)

func twoSum1(nums []int, target int) []int {
	for i := 0; i <= len(nums)-1; i++ {
		for j := i + 1; j <= len(nums)-1; j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return nil
}

func twoSum2(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	for i := 0; i <= len(nums)-1; i++ {
		m[nums[i]] = i
	}

	for j := 0; j <= len(nums)-1; j++ {
		if _, ok := m[target-nums[j]]; ok && m[target-nums[j]] != j {
			return []int{j, m[target-nums[j]]}
		}
	}
	return nil
}

func twoSum3(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	for i := 0; i <= len(nums)-1; i++ {
		if _, ok := m[target-nums[i]]; ok {
			return []int{m[target-nums[i]], i}
		}
		m[nums[i]] = i
	}
	return nil
}

func main() {
	result := twoSum2([]int{0, 4, 3, 0}, 0)
	fmt.Printf("%v\n", result)
}
