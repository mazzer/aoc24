from aoc24 import read_input_file

MOVEMENTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def read_file() -> list[list[int]]:
    return [list(map(int, list(line))) for line in read_input_file("day10")]


def part1() -> int:
    grid = read_file()

    rows, cols = len(grid), len(grid[0])

    def explore_hiking_trail(
        current_row: int, current_column: int, visited_positions: set[tuple[int, int]]
    ) -> int:
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
                and (next_row, next_column) not in visited_positions
            ):
                score += explore_hiking_trail(next_row, next_column, visited_positions)

        return score

    trailheads = [
        (row_index, column_index)
        for row_index in range(rows)
        for column_index in range(cols)
        if grid[row_index][column_index] == 0
    ]

    return sum(explore_hiking_trail(row, col, set()) for row, col in trailheads)


def part2(): ...


def solve():
    print(part1())
    print(part2())
