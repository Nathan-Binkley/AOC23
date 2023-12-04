package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if strings.TrimSpace(b) == a {
			if a != " " && a != "" && b != " " && b != "" {
				// fmt.Println("Found", a, b)
				return true
			}
		}
	}
	return false
}

type linereader struct {
	reader *bufio.Scanner
	_file  *os.File
	line   string
}

func processScratchCard(line string) ([]int, map[int]interface{}) {
	ourNums := make([]int, 0)
	winningNums := make(map[int]interface{})

	toProcess := strings.Split(line, ": ")[1]
	numbersStrings := strings.Split(toProcess, " | ")

	for _, num := range strings.Split(numbersStrings[1], " ") {
		if num == "" {
			continue
		}
		num_, _ := strconv.Atoi(num)
		ourNums = append(ourNums, num_)
	}

	for _, num := range strings.Split(numbersStrings[0], " ") {
		if num == "" {
			continue
		}
		num_, _ := strconv.Atoi(num)
		winningNums[num_] = new(interface{})
	}

	return ourNums, winningNums
}

func getLineReader(inputFile string) (linereader, error) {
	readFile, err := os.Open(inputFile)
	if err != nil {
		fmt.Println(err)
		return linereader{}, err
	}

	filescanner := bufio.NewScanner(readFile)
	filescanner.Split(bufio.ScanLines)
	reader := linereader{filescanner, readFile, ""}

	return reader, nil
}

func (lr *linereader) Line() string {
	return lr.line
}

func (lr *linereader) Next() bool {
	if lr.reader.Scan() {
		lr.line = lr.reader.Text()
		return true
	}
	return false
}

func sumOfNums(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}

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

	final := 0.
	have := 0

	scores := make([]int, 0)

	// Core logic goes here, one line at a time
	for scanner.Scan() {

		line := scanner.Text()
		all_numbers := strings.TrimSpace(strings.Split(line, ":")[1])
		winners := strings.Fields(strings.TrimSpace(strings.Split(all_numbers, "|")[0]))
		// fmt.Println(winners)
		numbers_you_have := strings.Fields(strings.TrimSpace(strings.Split(all_numbers, "|")[1]))
		for _, winner := range winners {
			// fmt.Println(winner, numbers_you_have, have)
			if winner != " " && winner != "" {
				if stringInSlice(strings.TrimSpace(winner), numbers_you_have) {
					have++
				}
			}
		}
		scores = append(scores, 1)

		// fmt.Println("Card Final:", have, math.Pow(2, float64(have)))
		if have > 1 {
			final += math.Pow(2, float64(have-1))
		} else if have == 1 {
			final += 1
		}
		have = 0
	}

	fmt.Println("Part 1:", final)
	scores = append(scores, 0)

	final = 0

	file, err = os.Open(os.Args[1])
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	scanner = bufio.NewScanner(file)

	reader, _ := getLineReader(os.Args[1])

	copies := make([]int, 1)
	copies[0] = 1
	copyIdx := 0

	for reader.Next() {
		ourNums, winningNums := processScratchCard(reader.Line())
		cardScore := 0
		for _, num := range ourNums {
			_, isWinning := winningNums[num]

			if isWinning {
				cardScore += 1
			}
		}

		for len(copies) < copyIdx+cardScore+1 {
			copies = append(copies, 1)
		}
		for j := 0; j < cardScore; j++ {
			copies[copyIdx+1+j] += copies[copyIdx]
		}
		copyIdx += 1

	}

	fmt.Println("Part 2:", sumOfNums(copies))
}
