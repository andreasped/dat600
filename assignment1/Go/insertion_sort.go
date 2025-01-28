package main

import (
	"fmt"
	"time"
)

func insertionSort(arr []int) {
	n := len(arr)

	if n <= 1 {
		return
	}

	// Iterate over the array starting from the second element
	for i := 1; i < n; i++ {
		key := arr[i]
		j := i - 1
		// Move elements greater than key one position ahead
		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j--
		}

		// Insert the key in the right position
		arr[j+1] = key
	}

	return
}

func main() {
	arrays := [][]int{}

	arr10 := make([]int, 10)
	for i := 0; i < 10; i++ {
		arr10[i] = 10 - i
	}
	
    arr100 := make([]int, 100)
    for i := 0; i < 100; i++ {
		arr100[i] = 100 - i
    }

	arr1000 := make([]int, 1000)
	for i := 0; i < 1000; i++ {
		arr1000[i] = 1000 - i
	}

	arrays = append(arrays, arr10, arr100, arr1000)

	times := []float64{}

	for _, arr := range arrays {
		timeStart := time.Now()
		insertionSort(arr)
		timeEnd := time.Now()
		times = append(times, float64(timeEnd.Sub(timeStart).Nanoseconds())/1e6)
	}

	fmt.Println("Time taken to sort array of size 10:", times[0], "ms")
	fmt.Println("Time taken to sort array of size 100:", times[1], "ms")
	fmt.Println("Time taken to sort array of size 1000:", times[2], "ms")
}
