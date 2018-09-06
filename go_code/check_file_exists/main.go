package main

import (
	"fmt"
	"os"
)

func main() {
	filename := "example.txt"
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		fmt.Println("File does not exist")
	} else {
		fmt.Println("File exists")
	}
}
