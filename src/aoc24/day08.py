from collections import defaultdict

from aoc24 import read_input_file


def read_file() -> list[str]:
    return read_input_file("day08")


def part1():
    grid = [list(line) for line in read_file()]
    rows, cols = len(grid), len(grid[0])

    antennas = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            cell = grid[row][col]
            if cell != ".":
                antennas[cell].append((row, col))

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


def part2(): ...


def solve():
    print(part1())
    print(part2())
