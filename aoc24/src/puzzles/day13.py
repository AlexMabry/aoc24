import re
import numpy as np
from ..utils import parse_data

PATTERN = re.compile(r".*X.(\d+), Y.(\d+)")


def parse_machine(data: list[str]):
    return [list(map(int, PATTERN.match(line).groups())) for line in data[:3]]


def find_min_coins(machines, offset=0):
    total = 0
    for A, B, P in machines:
        buttons = np.array(list(zip(A, B)))
        prize = np.array(P) + offset
        solution = np.linalg.solve(buttons, prize)
        if np.allclose(np.dot(buttons, solution.round(0)), prize, 1e-15, 1e-15):
            total += sum(solution.round(0) * (3, 1))

    return int(total)


def solve_part1(data: str):
    input_data = parse_data(data)
    machines = [parse_machine(input_data[l:]) for l in range(0, len(input_data), 4)]

    return find_min_coins(machines)


def solve_part2(data: str):
    input_data = parse_data(data)
    machines = [parse_machine(input_data[l:]) for l in range(0, len(input_data), 4)]

    return find_min_coins(machines, 10000000000000)
