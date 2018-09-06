package main

import (
	"fmt"
	"strings"
)

func main() {

	myString := "Hello! This is a golangcode.com test ;)"

	//Split
	fmt.Printf("%q\n", strings.Split(myString, " "))

	//Replace
	fmt.Println(strings.Replace(myString, "This", "That", 2))

	// bad way
	// Step 1: Convert it to a rune
	a := []rune(myString)

	// Step 2: Grab the num of chars you need
	myShortString := string(a[7:11])

	fmt.Println(myShortString)
}
