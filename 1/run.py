#!/usr/bin/env python3

"""https://adventofcode.com/2024/day/1"""

DEBUG = False


def read_file(index: int, sorted: bool) -> list[int]:
    """Read value from file and split accordingly"""
    filename = r"1/input.txt"
    f = open(filename, "r", encoding="utf-8")

    ret = []

    for line in f:
        ret.append(int(line.split("   ")[index]))

    if DEBUG:
        print(f"Values at position {index}: ", ret)

    if sorted:
        ret.sort()

        if DEBUG:
            print(f"Values at position {index} (sorted): ", ret)

    return ret


def compare_list(first: list[int], second: list[int]) -> int:
    """Calculate distance between the list"""
    size = len(first)
    distance = 0

    for i in range(size):
        distance += abs(first[i] - second[i])

    return distance


def calculate_simlilarity_score(first: list[int], second: list[int]) -> int:
    """Calculate similarity score between the list"""
    score = 0
    cache = {}

    for v in first:
        if v in cache:
            score += cache[v]
        else:
            s = second.count(v) * v
            cache[v] = s
            score += s

    return score


def main():
    """Main entry point"""
    first_list = read_file(0, False)
    second_list = read_file(1, False)

    # result = compare_list(first_list, second_list)
    result = calculate_simlilarity_score(first_list, second_list)

    print(f"Answer is {result}")


if __name__ == "__main__":
    main()
