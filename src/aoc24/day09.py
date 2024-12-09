from aoc24 import read_input_file


def read_file() -> list[str]:
    return read_input_file("day09")


def part1() -> int:
    s = 0

    for disk_map in read_file():
        file_idx = 0
        blocks = []

        for i, length in enumerate(map(int, disk_map)):
            if i % 2 == 0:
                blocks += [(str(file_idx),) for _ in range(length)]
                file_idx += 1
            else:
                blocks += [(".",) for _ in range(length)]

        last_index = 0
        for i in reversed(range(len(blocks))):
            if blocks[i] == ".":
                continue

            last_index = next(
                i for i in range(last_index, len(blocks)) if blocks[i][0] == "."
            )

            if last_index > i:
                break

            blocks[i], blocks[last_index] = blocks[last_index], blocks[i]

        s += sum(int(b) * i for i, (b, *_) in enumerate(blocks) if b != ".")

    return s


def part2(): ...


if __name__ == "__main__":
    print(part1())
    print(part2())
