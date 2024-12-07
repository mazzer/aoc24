from aoc24 import read_input_file


def read_file() -> tuple[list[list[int]], list[dict[int, int]]]:
    f = read_input_file("day05")

    rules, pages = [], []

    rule_mode = True
    for line in f:
        if line == "":
            rule_mode = False
            continue

        if rule_mode:
            rules.append(list(map(int, line.split("|"))))
        else:
            pages.append({int(num): 0 for num in line.split(",")})

    return rules, pages


def part1() -> int:
    rules, pages = read_file()

    median_sum = 0

    for page in pages:
        is_valid = True

        for rule_1, rule_2 in rules:
            if rule_1 not in page or rule_2 not in page:
                continue

            has_rule_1 = False
            for p in page:
                if not has_rule_1 and p == rule_1:
                    has_rule_1 = True
                    continue
                elif p == rule_2:
                    if not has_rule_1:
                        is_valid = False

                    break

            if not is_valid:
                break

        if is_valid:
            median_sum += list(page.keys())[int(len(page) / 2)]

    return median_sum


def part2(): ...


def solve():
    print(part1())
    print(part2())
