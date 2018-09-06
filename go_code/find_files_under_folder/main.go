package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	folder := `e:\`
	listFile(folder)
}

func listFile(folder string) {
	files, err := ioutil.ReadDir(folder) //specify the current dir
	if err != nil {
		log.Fatal(err)
	}
	for _, file := range files {
		if file.IsDir() {
			listFile(folder + "/" + file.Name())
		} else {
			fmt.Println(folder + "/" + file.Name())
		}
	}

}
