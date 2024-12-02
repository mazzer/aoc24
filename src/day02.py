from pathlib import Path
import itertools


def read_file() -> list[list[int]]:
    lines = (Path(__file__).parent.parent / "inputs/day02").read_text().splitlines()

    return [list(map(int, line.split())) for line in lines]


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


if __name__ == '__main__':
    print(part1())
    print(part2())
