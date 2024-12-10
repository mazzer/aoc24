from aoc24 import read_input_file

MOVEMENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def read_file() -> list[list[int]]:
    return [list(map(int, list(line))) for line in read_input_file("day10")]


def get_trailheads(grid: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (row_index, column_index)
        for row_index in range(len(grid))
        for column_index in range(len(grid[0]))
        if grid[row_index][column_index] == 0
    ]


def calculate_trail_metrics(
    grid,
    current_row: int,
    current_column: int,
    distinct: bool,
    visited_positions: set[tuple[int, int]] | None = None,
) -> int:
    if visited_positions is None:
        visited_positions = set()

    rows, cols = len(grid), len(grid[0])

    visited_positions.add((current_row, current_column))

    score = 0
    if grid[current_row][current_column] == 9:
        score += 1

    for row_offset, column_offset in MOVEMENTS:
        next_row, next_column = (
            current_row + row_offset,
            current_column + column_offset,
        )

        if (
            0 <= next_row < rows
            and 0 <= next_column < cols
            and grid[next_row][next_column] == grid[current_row][current_column] + 1
            and (distinct or (next_row, next_column) not in visited_positions)
        ):
            score += calculate_trail_metrics(
                grid, next_row, next_column, distinct, visited_positions
            )

    return score


def part1() -> int:
    grid = read_file()

    return sum(
        calculate_trail_metrics(grid, row, col, False)
        for row, col in get_trailheads(grid)
    )


def part2() -> int:
    grid = read_file()

    return sum(
        calculate_trail_metrics(grid, row, col, True)
        for row, col in get_trailheads(grid)
    )


def solve():
    print(part1())
    print(part2())
