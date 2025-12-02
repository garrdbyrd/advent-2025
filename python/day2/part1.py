# Advent of Code 2025
# Day 2

import os


def get_invalid_ids(min, max):
    invalid_ids = []
    if min == max:
        invalid_ids.append(min)
        return invalid_ids

    min_unit = int(str(min)[: int(len(str(min)) / 2)])
    max_unit = int(str(max)[: int(len(str(max)) / 2)])

    for i in range(min_unit, max_unit + 1):
        invalid_ids.append(int(str(i) + str(i)))

    return invalid_ids


def get_min(lower, upper):
    # odd
    if len(lower) % 2 == 1:
        unit = str(int(10 ** ((len(lower) - 1) / 2)))
        possible_min = unit + unit
    # even
    else:
        # check if lower bound is itself a repeated number
        if lower[: int(len(lower) / 2)] == lower[int(len(lower) / 2) :]:
            unit = lower[: int(len(lower) / 2)]
            possible_min = lower
        # if first half greater than second half,
        # then lowest possible repeated number is [first half : first half]
        # e.g., 123122 -> 123123
        elif int(lower[: int(len(lower) / 2)]) >= int(lower[int(len(lower) / 2) :]):
            unit = lower[: int(len(lower) / 2)]
            possible_min = unit + unit
        # if first half is less than second half,
        # then lowest possible repeated number is [first half + 1 : first half + 1]
        # e.g., 123321 -> 124124
        else:
            unit = str(int(lower[: int(len(lower) / 2)]) + 1)
            possible_min = unit + unit

    # make sure possible minimum is less than upper bound
    if int(possible_min) > int(upper):
        # print("no minimum in range")
        return None

    else:
        min = possible_min

    return int(min)


def get_max(lower, upper):
    # odd
    if len(upper) % 2 == 1:
        # 123 -> 99
        possible_max = str(int(10 ** (len(upper) - 1) - 1))
    # even
    else:
        # check if upper bound is max
        if upper[: int(len(upper) / 2)] == upper[int(len(upper) / 2) :]:
            unit = upper[: int(len(upper) / 2)]
            possible_max = upper
        # if first half greater than second half,
        # then greatest possible repeated number is [first half - 1 : first half - 1]
        # e.g., 123120 -> 122122
        elif int(upper[: int(len(upper) / 2)]) >= int(upper[int(len(upper) / 2) :]):
            unit = str(int(upper[: int(len(upper) / 2)]) - 1)
            possible_max = unit + unit
        # if first half is less than second half,
        # then greatest possible repeated number is [first half : first half]
        # e.g., 123321 -> 123123
        else:
            unit = upper[: int(len(upper) / 2)]
            possible_max = unit + unit

    # make sure possible maximum is greater than lower bound
    if int(possible_max) < int(lower):
        # print("no maximum in range")
        return None

    else:
        max = possible_max

    return int(max)


def check_range(range):
    # in
    lower = range[0]
    upper = range[1]
    # return
    invalid_ids = []

    min = get_min(lower, upper)
    max = get_max(lower, upper)

    if min and max:
        print(f"min/max:")
        print(f"    {min}")
        print(f"    {max}")
        invalid_ids = get_invalid_ids(min, max)
        return invalid_ids

    return []


def main():
    # input
    input_file = f"{os.path.dirname(os.path.realpath(__file__))}/input.txt"
    input_ranges = []

    invalid_ids = []

    input_string = ""
    with open(input_file, "r") as file:
        for line in file:
            input_string = line
            break

    for range in input_string.split(","):
        input_ranges.append(range.split("-"))

    for range in input_ranges:
        invalid_ids += check_range(range)

    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
