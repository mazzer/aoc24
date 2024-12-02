import itertools

from aoc24 import read_input_file


def read_file() -> list[list[int]]:
    return [list(map(int, line.split())) for line in read_input_file("day02")]


def check_report(reports: list[int]) -> bool:
    is_descending = reports[0] > reports[1]

    if sorted(reports, reverse=is_descending) != reports:
        return False

    return all(
        1 <= abs(reports[i] - reports[i + 1]) <= 3 for i in range(len(reports) - 1)
    )


def part1() -> int:
    return sum(check_report(report_line) for report_line in read_file())


def part2() -> int:
    safe_lines = 0

    for report_line in read_file():
        combinations = [report_line] + [
            list(combo)
            for combo in itertools.combinations(report_line, len(report_line) - 1)
        ]

        if any(check_report(combo) for combo in combinations):
            safe_lines += 1

    return safe_lines


def solve():
    print(part1())
    print(part2())
