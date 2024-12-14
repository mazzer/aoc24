import dataclasses
from typing import Self

from aoc24 import read_input_file

BTN_A_COST = 3
BTN_B_COST = 1


@dataclasses.dataclass
class Machine:
    a: complex
    b: complex
    prize: complex

    def add_prize_offset(self, offset: int) -> Self:
        self.prize += complex(offset, offset)

        return self


def read_file() -> list[Machine]:
    def parse(line, split_on: str):
        coords = line.split(": ")[1].split(", ")
        x = int(coords[0].split(f"X{split_on}")[1])
        y = int(coords[1].split(f"Y{split_on}")[1])

        return complex(x, y)

    lines = read_input_file("day13")

    machines = []

    for i in range(0, len(lines), 3):
        machine = Machine(
            parse(lines[i], "+"),
            parse(lines[i + 1], "+"),
            parse(lines[i + 2], "="),
        )

        machines.append(machine)

    return machines


def solve_machine(machine: Machine) -> int | None:
    determinant = (machine.a.conjugate() * machine.b).imag
    if determinant == 0:
        return None

    a_numerator = (machine.prize.conjugate() * machine.b).imag
    b_numerator = (machine.a.conjugate() * machine.prize).imag

    if a_numerator % determinant != 0 or b_numerator % determinant != 0:
        return None

    a = a_numerator // determinant
    b = b_numerator // determinant

    if a < 0 or b < 0:
        return None

    return int(BTN_A_COST * a + BTN_B_COST * b)


def part1() -> int:
    machines = read_file()

    costs = [solve_machine(machine) for machine in machines]

    return sum(c for c in costs if c is not None)


def part2() -> int:
    machines = read_file()

    offset = 10_000_000_000_000

    costs = [solve_machine(machine.add_prize_offset(offset)) for machine in machines]

    return sum(c for c in costs if c is not None)


def solve():
    print(part1())
    print(part2())
