from collections import Counter
from pathlib import Path


def read_file() -> tuple[list[int], list[int]]:
    lines = (Path(__file__).parent.parent / "inputs/day01").read_text().splitlines()
    left, right = zip(*[map(int, line.split()) for line in lines])

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


if __name__ == '__main__':
    print(part1())
    print(part2())
