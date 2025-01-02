import re
from itertools import groupby
from time import sleep

from ..utils import parse_data


PATTERN = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")


def move_robot(r, t=1, max_x=101, max_y=103):
    return (r[0] + r[2] * t) % max_x, (r[1] + r[3] * t) % max_y


def quadrant(r, mid_x=50, mid_y=51):
    return (
        None
        if r[0] == mid_x or r[1] == mid_y
        else (1 if r[0] > mid_x else 0) + (2 if r[1] > mid_y else 0)
    )


def solve_part1(data: str):
    input_data = parse_data(data)
    robots = [tuple(map(int, PATTERN.match(line).groups())) for line in input_data]
    moved_robots = [move_robot(r, 100) for r in robots]
    quadrants = [q for r in moved_robots if (q := quadrant(r)) is not None]
    per_quad = [len(list(g)) for k, g in groupby(sorted(quadrants))]
    return per_quad[0] * per_quad[1] * per_quad[2] * per_quad[3]


def solve_part2(data: str):
    input_data = parse_data(data)
    robots = [tuple(map(int, PATTERN.match(line).groups())) for line in input_data]
    seconds = 18
    robots = [(*move_robot(r, 18), r[2], r[3]) for r in robots]
    while True:
        seconds += 101
        robots = [(*move_robot(r, 101), r[2], r[3]) for r in robots]
        sr = set([(r[0], r[1]) for r in robots])

        print(f"Seconds: {seconds}")
        for y in range(51):
            print("".join(["x" if (x, y) in sr else "." for x in range(101)]), end="")
            print("".join(["x" if (x, y + 51) in sr else "." for x in range(101)]))

        print()
        sleep(0.1)

    return None
