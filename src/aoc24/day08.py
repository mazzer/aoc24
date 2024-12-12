from collections import defaultdict
from math import gcd

from aoc24 import read_input_file


def read_file() -> list[str]:
    return read_input_file("day08")


def get_antennas(grid):
    antennas = defaultdict(list)

    for row, line in enumerate(grid):
        for col, cell in enumerate(grid):
            cell = grid[row][col]
            if cell != ".":
                antennas[cell].append((row, col))

    return antennas


def part1():
    grid = [list(line) for line in read_file()]

    antennas = get_antennas(grid)

    rows, cols = len(grid), len(grid[0])

    antinodes = set()

    for antenna, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                difference = tuple(b - a for a, b in zip(positions[i], positions[j]))

                for index, direction in [(i, -1), (j, 1)]:
                    new_position = tuple(
                        pos + diff * direction
                        for pos, diff in zip(positions[index], difference)
                    )

                    if 0 <= new_position[0] < rows and 0 <= new_position[1] < cols:
                        antinodes.add(new_position)

    return len(antinodes)


def part2():
    grid = [list(line) for line in read_file()]

    antennas = get_antennas(grid)

    rows, cols = len(grid), len(grid[0])

    antinodes = set()

    for antenna, positions in antennas.items():
        antinodes.update(positions)

        for i, start in enumerate(positions):
            for j in range(i + 1, len(positions)):
                end = positions[j]
                difference = (end[0] - start[0], end[1] - start[1])

                step_gcd = gcd(difference[0], difference[1])
                step = (difference[0] // step_gcd, difference[1] // step_gcd)

                current = start
                while 0 <= current[0] < rows and 0 <= current[1] < cols:
                    antinodes.add(current)
                    current = (current[0] - step[0], current[1] - step[1])

                current = end
                while 0 <= current[0] < rows and 0 <= current[1] < cols:
                    antinodes.add(current)
                    current = (current[0] + step[0], current[1] + step[1])

    return len(antinodes)


def solve():
    print(part1())
    print(part2())
