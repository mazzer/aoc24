from functools import cache

from aoc24 import read_input_file


def read_file() -> list[int]:
    return [list(map(int, list(line.split()))) for line in read_input_file("day11")][0]


def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        half = len(str(stone)) // 2
        return [int(str(stone)[:half]), int(str(stone)[half:])]

    return [stone * 2024]


@cache
def count_splits(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    return sum(count_splits(s, blinks - 1) for s in blink(stone))


def part1() -> int:
    return sum(count_splits(stone, 25) for stone in read_file())


def part2():
    return sum(count_splits(stone, 75) for stone in read_file())


def solve():
    print(part1())
    print(part2())
