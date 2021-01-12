package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func check(e error) {
	// Panics if an error is detected
	if e != nil {
		panic(e)
	}
}

func main() {

	// Program is read into an array
	if len(os.Args) == 1 {
		fmt.Println("USAGE: program [OPTIONS] file")
		os.Exit(1)
	}

	bfFile, err := ioutil.ReadFile(os.Args[len(os.Args)-1])
	check(err)

	// Program is cleaned of whitespace and unecessary characters
	program := cleanFile(string(bfFile))

	// Allocating a map for instruction jumping
	loops := []int{}
	loopMap := make(map[int]int)

	// Generating the loop jump map here
	for instruction, command := range program {
		if command == '[' {
			loops = append(loops, instruction)
		} else if command == ']' {
			var opening int
			loops, opening = loops[:len(loops)-1], loops[len(loops)-1]
			loopMap[opening], loopMap[instruction] = instruction, opening
		}
	}

	instruction := 0

	// Array allocation
	array := [30000]int{}
	dataPointer := 0

	for instruction < len(program) {
		command := program[instruction]

		// Handling different commands here
		if command == '>' {
			dataPointer++
		} else if command == '<' {
			dataPointer--
		} else if command == '+' {
			array[dataPointer]++
		} else if command == '-' {
			array[dataPointer]--
		} else if command == '.' {
			fmt.Print(string(array[dataPointer]))
		} else if command == ',' {
			// Input; have to implement it later
		} else if command == '[' {
			if array[dataPointer] == 0 {
				instruction = loopMap[instruction]
			}
		} else if command == ']' {
			if array[dataPointer] > 0 {
				instruction = loopMap[instruction]
			}
		}

		instruction++
	}

}

func cleanFile(bfFile string) string {
	// Cleans the input file
	var formattedFile strings.Builder

	for _, c := range bfFile {
		c := string(c)
		if strings.Contains("<>+-.,[]", c) {
			formattedFile.WriteString(c)
		}
	}

	return formattedFile.String()
}
