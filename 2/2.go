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

	possible_rounds := []int{}
	final := 0
	r := 12
	b := 14
	g := 13

	// Core logic goes here, one line at a time
	for scanner.Scan() {

		line := scanner.Text()
		game := strings.Split(line, ":")      // split line into block and game id
		rounds := strings.Split(game[1], ";") // split line into groupings

		possible := true

		for _, round := range rounds {

			colors := strings.Split(round, ",") // split line into colors + numbers

			for _, color := range colors {
				number := strings.Split(strings.TrimSpace(color), " ")[0]

				if strings.Contains(color, "red") {
					red, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if red > r {
						possible = false
						break
					}
				} else if strings.Contains(color, "blue") {
					blue, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if blue > b {
						possible = false
						break
					}

				} else if strings.Contains(color, "green") {
					green, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if green > g {
						possible = false
						break
					}

				}
			}
			if !possible {
				break
			}

		}
		if possible {
			game_number, err := strconv.Atoi(strings.Split(game[0], " ")[1])
			if err != nil {
				fmt.Println(err)
				os.Exit(1)
			}
			possible_rounds = append(possible_rounds, game_number)
		}

	}
	for _, round := range possible_rounds {
		final += round
	}
	fmt.Println("Part 1: ", final)

	possible_rounds = []int{}
	final = 0
	r = 0
	b = 0
	g = 0

	file, err = os.Open(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	scanner = bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		game := strings.Split(line, ":")      // split line into block and game id
		rounds := strings.Split(game[1], ";") // split line into groupings

		for _, round := range rounds {

			colors := strings.Split(round, ",") // split line into colors + numbers

			for _, color := range colors {
				number := strings.Split(strings.TrimSpace(color), " ")[0]

				if strings.Contains(color, "red") {
					red, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if red > r {
						r = red
					}
				} else if strings.Contains(color, "blue") {
					blue, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if blue > b {
						b = blue
					}

				} else if strings.Contains(color, "green") {
					green, _ := strconv.Atoi(string(strings.TrimSpace(number)))
					if green > g {
						g = green
					}

				}
			}

		}
		game_power := r * b * g
		possible_rounds = append(possible_rounds, game_power)
		r, g, b = 0, 0, 0
	}
	for _, round := range possible_rounds {
		final += round
	}
	fmt.Println("Part 2: ", final)
}
