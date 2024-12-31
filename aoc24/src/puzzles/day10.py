from functools import reduce

from ..utils import parse_data


def get_neighbors(x, y):
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]


def count_trails(grid, x, y, h=0):
    neighbors = {n for n in get_neighbors(x, y) if n in grid and grid[n] == h + 1}
    if h == 8:
        return neighbors
    else:
        return reduce(
            lambda a, b: a.union(b),
            (count_trails(grid, nx, ny, h + 1) for nx, ny in neighbors),
            set(),
        )


def solve_part1(data: str):
    parsed = parse_data(data)
    grid = {(x, y): int(c) for y, row in enumerate(parsed) for x, c in enumerate(row)}
    trailheads = [(x, y) for (x, y), h in grid.items() if h == 0]
    return sum(len(count_trails(grid, *t)) for t in trailheads)


def count_distinct_trails(grid, x, y, h=0):
    neighbors = {n for n in get_neighbors(x, y) if n in grid and grid[n] == h + 1}
    if h == 8:
        return len(neighbors)
    else:
        return sum([count_distinct_trails(grid, nx, ny, h + 1) for nx, ny in neighbors])


def solve_part2(data: str):
    parsed = parse_data(data)
    grid = {(x, y): int(c) for y, row in enumerate(parsed) for x, c in enumerate(row)}
    trailheads = [(x, y) for (x, y), h in grid.items() if h == 0]
    return sum(count_distinct_trails(grid, *t) for t in trailheads)
