import itertools

from aoc24 import read_input_file

OPERATORS = ["+", "*", "||"]


def read_file() -> list[tuple[int, list[int]]]:
    result = []

    for line in read_input_file("day07"):
        expected_sum, line = line.split(": ")

        result.append((int(expected_sum), list(map(int, line.split()))))

    return result


def check_line(expected_sum: int, line: list[int], concat_op=False) -> bool:
    for operators in itertools.product(OPERATORS, repeat=len(line) - 1):
        result = line[0]

        for i, op in enumerate(operators, start=1):
            match op:
                case "+":
                    result += line[i]
                case "*":
                    result *= line[i]
                case "||" if concat_op:
                    result = int(str(result) + str(line[i]))

            if result > expected_sum:
                break

        if result == expected_sum:
            return True

    return False


def part1() -> int:
    r = 0
    for expected_sum, line in read_file():
        if check_line(expected_sum, line):
            r += expected_sum

    return r


def part2():
    r = 0
    for expected_sum, line in read_file():
        if check_line(expected_sum, line, concat_op=True):
            r += expected_sum

    return r


print(part1())
print(part2())
