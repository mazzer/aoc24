from aoc24 import read_input_file

MOVEMENTS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_file() -> list[str]:
    return read_input_file("day06")


def part1() -> int:
    visited_positions = simulate_guard_movement()

    return len(visited_positions)


def simulate_guard_movement():
    grid = read_file()

    for row_idx, row in enumerate(grid):
        if (col_idx := row.find("^")) != -1:
            guard_pos = (row_idx, col_idx)
            break

    visited_positions = {guard_pos}
    direction = MOVEMENTS[0]

    while True:
        new_position: tuple[int, int] = (
            guard_pos[0] + direction[0],
            guard_pos[1] + direction[1],
        )

        if (
            new_position[0] < 0
            or new_position[0] >= len(grid)
            or new_position[1] < 0
            or new_position[1] >= len(grid[0])
        ):
            break

        if grid[new_position[0]][new_position[1]] == "#":
            direction = MOVEMENTS[(MOVEMENTS.index(direction) + 1) % 4]
            continue

        visited_positions.add(new_position)
        guard_pos = new_position

    return visited_positions


def part2():
    visited_positions = simulate_guard_movement()

    for row_idx, col_idx in visited_positions:
        pass

    return len(visited_positions)


def part2(): ...


def solve():
    print(part1())
    print(part2())
