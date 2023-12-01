package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage : " + os.Args[0] + " filename")
		os.Exit(1)
	}

	file, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	scanner := bufio.NewScanner(file)

	final := 0
	out := 0

	// Core logic goes here, one line at a time
	// for scanner.Scan() {

	// 	line := scanner.Text()

	// 	// blocks := strings.Split(line, " ") // split line into words
	// 	first := "1"
	// 	last := "1"
	// 	for _, letter := range strings.Split(line, "") {

	// 		i, err := strconv.Atoi(letter)
	// 		if err != nil {
	// 			_ = i
	// 			continue
	// 		}

	// 		if first == "" {
	// 			first = letter
	// 		}

	// 		last = letter

	// 	}
	// 	out, err = strconv.Atoi(first + last)

	// 	if err != nil {
	// 		fmt.Println(err)
	// 		os.Exit(1)
	// 	}
	// 	final += out
	// 	fmt.Println(line, out)
	// }
	// fmt.Println("Part 1: ", final)

	final = 0
	for scanner.Scan() { // part 2
		// fmt.Println("LINE:", scanner.Text())
		line := scanner.Text()
		buffer := []string{}

		// blocks := strings.Split(line, " ") // split line into words
		first := ""
		last := ""
		current := ""
		for _, letter := range strings.Split(line, "") {

			buffer = append(buffer, letter)
			current = ""

			// fmt.Println(buffer, current)

			i, err := strconv.Atoi(letter) // check if number
			if err != nil {                // if not number, try and convert to number
				// fmt.Println(err)
				_ = i
				if strings.Contains(strings.Join(buffer, ""), "one") {
					current = "1"
					buffer = []string{"e"}
				}
				if strings.Contains(strings.Join(buffer, ""), "two") {
					current = "2"
					buffer = []string{"o"}
				}
				if strings.Contains(strings.Join(buffer, ""), "three") {
					current = "3"
					buffer = []string{"e"}
				}
				if strings.Contains(strings.Join(buffer, ""), "four") {
					current = "4"
					buffer = []string{"r"}
				}
				if strings.Contains(strings.Join(buffer, ""), "five") {
					current = "5"
					buffer = []string{"e"}
				}
				if strings.Contains(strings.Join(buffer, ""), "six") {
					current = "6"
					buffer = []string{"x"}
				}
				if strings.Contains(strings.Join(buffer, ""), "seven") {
					current = "7"
					buffer = []string{"n"}
				}
				if strings.Contains(strings.Join(buffer, ""), "eight") {
					current = "8"
					buffer = []string{"t"}
				}
				if strings.Contains(strings.Join(buffer, ""), "nine") {
					current = "9"
					buffer = []string{"e"}
				}
				if strings.Contains(strings.Join(buffer, ""), "zero") {
					current = "0"
					buffer = []string{}
				}
				//if number converted successfully, set to first and last
				if current != "" && first == "" {
					first = current
				}
				if current != "" {
					last = current
				}
			} else {

				if first == "" {
					first = letter
				}

				last = letter
			}

			// fmt.Printf("first: %s, last: %s\n", first, last, )
		}

		out, err = strconv.Atoi(first + last)

		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}

		final += out
		fmt.Println("FINAL:", line, out)
	}

	fmt.Println("Part 2: ", final)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
