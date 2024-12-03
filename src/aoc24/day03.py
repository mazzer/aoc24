import re

from aoc24 import get_file_contents


def read_file() -> str:
    return get_file_contents("day03")


def part1() -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(a) * int(b) for a, b in pattern.findall(read_file()))


def part2():
    pattern = re.compile(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))")

    result = 0
    should_multiply = True
    for instruction, a, b in pattern.findall(read_file()):
        match instruction:
            case "do()":
                should_multiply = True
            case "don't()":
                should_multiply = False
            case _ if should_multiply:
                result += int(a) * int(b)

    return result


def solve():
    print(part1())
    print(part2())
