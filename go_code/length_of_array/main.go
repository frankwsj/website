package main

import "fmt"

func main() {

	// Create an exmaple array
	array := []int{1, 2, 3, 4, 5, 7, 8}

	// Print number of items
	fmt.Println("First Length:", len(array))

	// Add an item and print again
	array = append(array, 6)
	fmt.Println("Second Length:", len(array))
}
