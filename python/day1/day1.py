# Advent of Code 2025
# Day 1

import os

class Lock:
    def __init__(self):
        self.numbers = list(range(0,100))
        self.current_number = 50
        self.zero_counter = 0

    def _rotate(self, direction, distance):
        if direction == "L":
            self.current_number = (self.current_number - distance) % 100
        elif direction == "R":
            self.current_number = (self.current_number + distance) % 100
        else:
            raise ValueError("Bad direction. Must be either 'L' or 'R'")

    def rotate(self, input):
        direction = input[0]
        distance = int(input[1:])
        self._rotate(direction, distance)
        if self.current_number == 0:
            self.zero_counter += 1

    def print_zero_counter(self):
        print(self.zero_counter)


def main():
    input_file = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    input_list = []

    with open(input_file, "r") as file:
        for line in file:
            input_list.append(line[:-1])

    combination_lock = Lock()

    for input in input_list:
        combination_lock.rotate(input)

    combination_lock.print_zero_counter()

if __name__ == "__main__":
    main()