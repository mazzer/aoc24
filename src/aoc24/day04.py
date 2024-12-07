from collections import defaultdict

from aoc24 import read_input_file


def read_file() -> list[str]:
    return read_input_file("day04")


def find_diagonals(grid):
    lr_diagonals = defaultdict(list)
    rl_diagonals = defaultdict(list)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            lr_diagonals[row - col].append(grid[row][col])
            rl_diagonals[row + col].append(grid[row][col])

    return lr_diagonals, rl_diagonals


def part1() -> int:
    input_file = read_file()

    lines = input_file.copy()

    vertical_lines = [
        "".join([row[i] for row in input_file]) for i in range(len(input_file[0]))
    ]
    lines.extend(vertical_lines)

    lr_diagonals, rl_diagonals = find_diagonals(input_file)
    lines.extend(["".join(line) for line in lr_diagonals.values()])
    lines.extend(["".join(line) for line in rl_diagonals.values()])

    return sum(line.count("XMAS") + line.count("SAMX") for line in lines)


def part2(): ...


def solve():
    print(part1())
    print(part2())
