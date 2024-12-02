from collections import Counter

from aoc24 import read_input_file


def read_file() -> tuple[list[int], list[int]]:
    left, right = zip(*[map(int, line.split()) for line in read_input_file("day01")])

    return sorted(left), sorted(right)


def part1() -> int:
    return sum([abs(left - right) for left, right in zip(*read_file())])


def part2() -> int:
    left, right = read_file()

    occurrences = Counter(right)
    score = 0

    for v in left:
        score += v * occurrences.get(v, 0)

    return score


def solve():
    print(part1())
    print(part2())
