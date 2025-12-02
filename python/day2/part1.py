# Advent of Code 2025
# Day 2

import os


def main():
    # input
    input_file = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    input_ranges = []

    input_string = ""
    with open(input_file, "r") as file:
        for line in file:
            input_string = line
            break

    print(input_string)


if __name__ == "__main__":
    main()
