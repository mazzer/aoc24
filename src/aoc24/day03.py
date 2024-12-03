import re

from aoc24 import get_file_contents


def read_file() -> str:
    return get_file_contents("day03")


def part1() -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(a) * int(b) for a, b in pattern.findall(read_file()))


def part2():
    result = 0
    pattern = re.compile(r"mul\((\d+),(\d+)\)")

    line = read_file()
    should_multiply = True

    while line:
        if should_multiply:
            if (read_to := line.find("don't()")) == -1:
                read_to = len(line)

            result += sum(int(a) * int(b) for a, b in pattern.findall(line[:read_to]))

            line = line[read_to:]
            should_multiply = False
        else:
            line = line[line.find("do()") :]
            should_multiply = True

    return result


def solve():
    print(part1())
    print(part2())
