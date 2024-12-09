from aoc24 import read_input_file

EMPTY_SPACE = -1


def read_file() -> str:
    return read_input_file("day09")[0]


def generate_blocks():
    disk_map = read_file()

    file_idx = 0
    blocks = []
    for i, length in enumerate(map(int, disk_map)):
        if i % 2 == 0:
            blocks.append((file_idx, length))
            file_idx += 1
        else:
            blocks.append((EMPTY_SPACE, length))

    return blocks


def move_blocks(blocks, idx_first_empty_space, idx_file_block):
    size_difference = blocks[idx_first_empty_space][1] - blocks[idx_file_block][1]

    if size_difference == 0:
        blocks[idx_file_block], blocks[idx_first_empty_space] = (
            blocks[idx_first_empty_space],
            blocks[idx_file_block],
        )

        idx_file_block -= 1
    elif size_difference > 0:
        file_block = blocks.pop(idx_file_block)

        blocks[idx_first_empty_space] = (EMPTY_SPACE, size_difference)
        blocks.insert(idx_first_empty_space, file_block)
        blocks.insert(idx_file_block + 1, (EMPTY_SPACE, file_block[1]))

        idx_file_block -= 1
    elif size_difference < 0:
        file_block = blocks[idx_file_block]
        empty_block = blocks.pop(idx_first_empty_space)

        blocks.insert(idx_first_empty_space, (file_block[0], empty_block[1]))
        blocks[idx_file_block] = (file_block[0], file_block[1] - empty_block[1])
        blocks.insert(idx_file_block + 1, empty_block)

    return idx_file_block


def part1() -> int:
    blocks = generate_blocks()

    first_empty_block = 0
    i = len(blocks) - 1

    while True:
        if blocks[i][0] == EMPTY_SPACE:
            i -= 1
            continue

        first_empty_block = next(
            i
            for i in range(first_empty_block, len(blocks))
            if blocks[i][0] == EMPTY_SPACE
        )

        if first_empty_block is None or first_empty_block > i:
            i -= 1

            break

        i = move_blocks(blocks, first_empty_block, i)

    return sum(
        i * v
        for i, v in enumerate(
            val
            for value, length in blocks
            for val in [value] * length
            if value != EMPTY_SPACE
        )
    )


def part2() -> int:
    blocks = generate_blocks()

    i = len(blocks) - 1

    while i:
        if blocks[i][0] == EMPTY_SPACE:
            i -= 1
            continue

        first_empty_block = next(
            (
                idx
                for idx in range(0, len(blocks))
                if blocks[idx][0] == EMPTY_SPACE and blocks[idx][1] >= blocks[i][1]
            ),
            None,
        )

        if first_empty_block is None or first_empty_block > i:
            i -= 1
            continue

        i = move_blocks(blocks, first_empty_block, i)

    return sum(
        i * v
        for i, v in enumerate(
            val for value, length in blocks for val in [value] * length
        )
        if v != EMPTY_SPACE
    )


def solve():
    print(part1())
    print(part2())
